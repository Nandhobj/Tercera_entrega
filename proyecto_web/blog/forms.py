from django import forms
from .models import Autor, Post, Comentario


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class PostForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Post
        fields = '__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'


class BuscarPostForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)
