from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Page


class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "pages"


class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = "pages/page_form.html"
    fields = ("title", "subtitle", "content", "image")
    success_url = reverse_lazy("pages:page_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageAuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        page = self.get_object()
        return page.author == self.request.user


class PageUpdateView(LoginRequiredMixin, PageAuthorRequiredMixin, UpdateView):
    model = Page
    template_name = "pages/page_form.html"
    fields = ("title", "subtitle", "content", "image")

    def get_success_url(self):
        return reverse_lazy("pages:page_detail", kwargs={"pk": self.object.pk})


class PageDeleteView(LoginRequiredMixin, PageAuthorRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("pages:page_list")
