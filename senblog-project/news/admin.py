from django.contrib import admin
from .models import Kategori, Berita
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['nama']

class BeritaAdminForm(forms.ModelForm):
    konten = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Berita
        fields = '__all__'

class BeritaAdmin(admin.ModelAdmin):
    form = BeritaAdminForm
    list_display = ('judul', 'kategori', 'created_at')
    search_fields = ('judul', 'konten')
    list_filter = ('kategori', 'created_at')
    fields = ['judul', 'kategori', 'konten', 'gambar']


admin.site.register(Kategori)
admin.site.register(Berita, BeritaAdmin)
