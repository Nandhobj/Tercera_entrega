from django import forms
from django.contrib.auth import get_user_model

from .models import Message

User = get_user_model()


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("recipient", "subject", "body")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["recipient"].queryset = User.objects.exclude(pk=user.pk)

