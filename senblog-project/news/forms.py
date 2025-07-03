# news/forms.py
from django import forms
from .models import Berita
from ckeditor.widgets import CKEditorWidget

class BeritaForm(forms.ModelForm):
    class Meta:
        model = Berita
        fields = ['judul', 'kategori', 'konten']
        widgets = {
            'konten': CKEditorWidget(),
        }
