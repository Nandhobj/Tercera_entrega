from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import MessageCreateForm
from .models import Message


class InboxListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/inbox.html"
    context_object_name = "inbox_messages"

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)


class SentListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/sent.html"
    context_object_name = "sent_messages"

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)


class MessageAccessMixin(UserPassesTestMixin):
    def test_func(self):
        message = self.get_object()
        user = self.request.user
        return message.sender_id == user.id or message.recipient_id == user.id


class MessageDetailView(LoginRequiredMixin, MessageAccessMixin, DetailView):
    model = Message
    template_name = "messaging/detail.html"
    context_object_name = "message"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.recipient_id == self.request.user.id and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=["is_read"])
        return obj


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = "messaging/compose.html"
    success_url = reverse_lazy("messaging:sent")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
