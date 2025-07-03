from django.shortcuts import render, get_object_or_404
from .models import Berita, Kategori
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  # ⬅️ Tambahan untuk dashboard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import BeritaForm
from django.contrib import messages
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Langsung login setelah berhasil register
            return redirect('dashboard')  # Arahkan ke dashboard setelah daftar
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ✅ Halaman Beranda
def home(request):
    query = request.GET.get('q')
    kategori_id = request.GET.get('kategori')

    berita_list = Berita.objects.all().order_by('-created_at')

    if query:
        berita_list = berita_list.filter(judul__icontains=query)

    if kategori_id:
        berita_list = berita_list.filter(kategori_id=kategori_id)

    # ➕ Ambil berita terbaru (pertama)
    berita_terbaru = berita_list.first() if berita_list.exists() else None

    # Hilangkan berita terbaru dari daftar utama agar tidak dobel
    if berita_terbaru:
        berita_list = berita_list.exclude(id=berita_terbaru.id)

    # ➕ Pagination: tampilkan 5 berita per halaman
    paginator = Paginator(berita_list, 5)
    page_number = request.GET.get('page')
    berita = paginator.get_page(page_number)

    kategori = Kategori.objects.all()

    try:
        selected_kategori = int(kategori_id) if kategori_id else None
    except ValueError:
        selected_kategori = None

    return render(request, 'home.html', {
        'berita': berita,
        'kategori': kategori,
        'selected_kategori': selected_kategori,
        'berita_terbaru': berita_terbaru,
    })

# ✅ Detail Berita
def berita_detail(request, pk):
    berita = get_object_or_404(Berita, pk=pk)
    return render(request, 'berita_detail.html', {'berita': berita})

# ✅ Dashboard Pengguna
@login_required
def dashboard(request):
    berita_user = Berita.objects.all()  # Bisa difilter berdasarkan user jika modelnya mendukung
    return render(request, 'dashboard.html', {'berita_user': berita_user})

def tambah_berita(request):
    if request.method == 'POST':
        form = BeritaForm(request.POST)
        if form.is_valid():
            berita = form.save(commit=False)
            berita.save()
            messages.success(request, "Berita berhasil ditambahkan.")
            return redirect('dashboard')
    else:
        form = BeritaForm()
    return render(request, 'tambah_berita.html', {'form': form})