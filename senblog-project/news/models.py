from django.db import models
from ckeditor.fields import RichTextField

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Kategori"

    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    konten = RichTextField()  # Gunakan CKEditor
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar/', blank=True, null=True)

    def __str__(self):
        return self.judul
