#Şerife Nazlı Ünay
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random

form = Tk()
form.title('Sıralama Otomasyonu')
form.attributes('-fullscreen', True)

orijinal_liste = []  # Orijinal listeyi burada global olarak saklayacağız
siralanmis_liste = []
def ana_menu():
    temizle()
    form.config(bg="#f0f4f8")

    # Başlık Frame
    baslik_frame = Frame(form, bg="#0f172a", pady=20)
    baslik_frame.pack(fill="x")
    Label(baslik_frame,
          text="Sıralama Otomasyonu",
          font=("Consolas", 30, "bold"),
          fg="white", bg="#0f172a").pack()

    # Bilgilendirme metni
    info = ("Veri setinizi yükleyin veya oluşturun.\n"
            "Sonra istediğiniz sıralama algoritmasını seçin.")
    Label(form, text=info, font=("Segoe UI", 14), bg="#f0f4f8", fg="#334155").pack(pady=15)

    # Butonlar çerçevesi
    frame_buttons = Frame(form, bg="#f0f4f8")
    frame_buttons.pack(pady=10)

    def stil(renk):
        return {
            "font": ("Segoe UI", 14, "bold"),
            "bg": renk,
            "fg": "white",
            "activebackground": "#334155",
            "activeforeground": "white",
            "bd": 0,
            "width": 22,
            "height": 2,
            "relief": "ridge",
            "cursor": "hand2",
        }

    Button(frame_buttons, text="Dosyadan Oku", command=dosyadan_oku, **stil("#2563eb")).grid(row=0, column=0, padx=10, pady=10)
    Button(frame_buttons, text="Rastgele Oluştur", command=rastgele_olustur, **stil("#16a34a")).grid(row=0, column=1, padx=10, pady=10)
    Button(frame_buttons, text="Kullanıcıdan Al", command=kullanicidan_al, **stil("#f97316")).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_buttons, text="Çıkış", command=form.quit, **stil("#dc2626")).grid(row=1, column=1, padx=10, pady=10)

    # Alt kısım - sürüm ve not alanı
    alt_frame = Frame(form, bg="#e2e8f0", pady=10)
    alt_frame.pack(fill="x", side="bottom")

    Label(alt_frame, text="© 2025 Şerife Nazlı Ünay | Sıralama Otomasyonu v1.0",
          font=("Segoe UI", 10), bg="#e2e8f0", fg="#475569").pack()

    form.eval('tk::PlaceWindow . center')

def aralik_kontrol(liste, alt=1, ust=70):
    # Listedeki tüm sayılar alt ve üst aralıkta mı kontrol eder
    for sayi in liste:
        if sayi < alt or sayi > ust:
            return False
    return True
def temizle():
    for widget in form.winfo_children():
        widget.destroy()
def save_list():
    global siralanmis_liste
    if not siralanmis_liste:
        messagebox.showwarning("Uyarı", "Önce bir sıralama yapınız!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(", ".join(map(str, siralanmis_liste)))  # Burada düzeltme yapıldı
        print(f"Liste {file_path} dosyasına kaydedildi.")
def verileri_goster(liste, baslik="Veriler", orijinal_kaydet=True):
    global orijinal_liste
    temizle()
    Label(form, text=baslik, font="Helvetica 16 bold", bg="#f97316").pack(pady=10)

    for sayi in liste:
        uzunluk = sayi * 10
        Label(form, text=str(sayi), font="Helvetica 12", bg="white", fg="#f97316", width=10).pack(pady=5, ipadx=uzunluk)

    if orijinal_kaydet:
        orijinal_liste = liste[:]  # Listeyi kopyalayarak orijinal halini kaydet

    siralama_menusu()

def dosyadan_oku():
    try:
        dosya_yolu = filedialog.askopenfilename(
            title="Bir .txt dosyası seçin",
            filetypes=(("Text dosyaları", "*.txt"), ("Tüm dosyalar", "*.*"))
        )
        if not dosya_yolu:
            return  # Kullanıcı iptal etti

        with open(dosya_yolu, "r") as dosya:
            veri = dosya.read()

        liste = [int(x.strip()) for x in veri.split(",") if x.strip().isdigit()]

        if not aralik_kontrol(liste):
            messagebox.showerror("Hata", "Dosyadaki sayılar 1 ile 70 arasında olmalıdır.")
            return

        verileri_goster(liste, "Dosyadan Okunan Veriler")
    except FileNotFoundError:
        messagebox.showerror("Hata", "Dosya bulunamadı.")
    except ValueError:
        messagebox.showerror("Hata", "Dosyada hatalı veri bulundu.")

def rastgele_olustur():
    liste = [random.randint(1, 70) for _ in range(10)]
    verileri_goster(liste, "Rastgele Oluşturulan Veriler")

def kullanicidan_al():
    temizle()
    form.config(bg="#0f172a")

    # Orta kısım için bir frame oluşturuyoruz, form içinde ortalanacak
    orta_frame = Frame(form, bg="#0f172a")
    orta_frame.pack(expand=True)  # Ekranın ortasına genişleyerek konumlanır

    Label(orta_frame,
          text="Sayıları virgül ile ayırarak girin:",
          font=("Helvetica", 18, "bold"),
          fg="white", bg="#0f172a").pack(pady=(0, 20))

    entry = Entry(orta_frame,
                  font=("Helvetica", 14),
                  width=30,
                  bg="#1e293b",  # Koyu gri-mavi arkaplan
                  fg="white",
                  insertbackground="white",  # İmleç rengi
                  relief="flat",
                  highlightthickness=2,
                  highlightcolor="#f97316",
                  highlightbackground="#475569",
                  bd=0)
    entry.pack(pady=10, ipady=8)  # ipady ile iç yükseklik artırıldı

    def veri_al():
        try:
            veri = entry.get()
            liste = [int(x.strip()) for x in veri.split(",") if x.strip().isdigit()]
            if not liste:
                raise ValueError
            if not aralik_kontrol(liste):
                messagebox.showerror("Hata", "Lütfen 1 ile 70 arasında sayılar girin.")
                return
            verileri_goster(liste, "Kullanıcıdan Alınan Veriler")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

    Button(orta_frame,
           text="Gönder",
           font=("Helvetica", 14, "bold"),
           command=veri_al,
           bg="#f97316",
           fg="white",
           activebackground="#c2410c",
           activeforeground="white",
           relief="flat",
           cursor="hand2",
           width=20,
           height=2
           ).pack(pady=(25, 10))

    Button(orta_frame,
           text="Ana Menüye Dön",
           font=("Helvetica", 14, "bold"),
           command=ana_menu,
           bg="#dc2626",
           fg="white",
           activebackground="#991b1b",
           activeforeground="white",
           relief="flat",
           cursor="hand2",
           width=20,
           height=2
           ).pack(pady=(0, 10))



def siralama_menusu():
    global orijinal_liste
    form.config(bg="#0f172a")

    Label(form,
          text="Sıralama Yöntemleri",
          font=("Helvetica", 18, "bold"),
          bg="#0f172a",
          fg="white").pack(pady=(20, 15))

    # İlk satır frame - 3 buton
    frame_sirala_ust = Frame(form, bg="#0f172a")
    frame_sirala_ust.pack(pady=5)

    # İkinci satır frame - 3 buton
    frame_sirala_alt = Frame(form, bg="#0f172a")
    frame_sirala_alt.pack(pady=5)

    # Buton stili
    btn_style = {
        "font": ("Helvetica", 13, "bold"),
        "bg": "#f97316",
        "fg": "white",
        "activebackground": "#c2410c",
        "activeforeground": "white",
        "relief": "flat",
        "cursor": "hand2",
        "width": 16,
        "height": 2,
        "bd": 0,
        "highlightthickness": 0,
    }

    # Üst satır butonları
    Button(frame_sirala_ust, text="Insertion Sort", command=lambda: insertion_sort(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)
    Button(frame_sirala_ust, text="Bubble Sort", command=lambda: bubble_sort(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)
    Button(frame_sirala_ust, text="Selection Sort", command=lambda: selection_sort(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)

    # Alt satır butonları
    Button(frame_sirala_alt, text="Heap Sort", command=lambda: heap_sort(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)
    Button(frame_sirala_alt, text="Radix Sort", command=lambda: radix_sort(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)
    Button(frame_sirala_alt, text="Counting Sort", command=lambda: counting_sort_wrapper(orijinal_liste[:]), **btn_style).pack(side=LEFT, padx=10)

    # Alt kısım butonları frame
    frame_alt = Frame(form, bg="#0f172a")
    frame_alt.pack(pady=30)
    btn_save_style = {
        "font": ("Helvetica", 14, "bold"),
        "bg": "white",
        "fg": "green",
        "activebackground": "#c2410c",
        "activeforeground": "white",
        "relief": "flat",
        "cursor": "hand2",
        "width": 14,
        "height": 2,
        "bd": 0,
        "highlightthickness": 0,
    }
    btn_reset_style = {
        "font": ("Helvetica", 14, "bold"),
        "bg": "white",
        "fg": "#2563eb",
        "activebackground": "#c2410c",
        "activeforeground": "white",
        "relief": "flat",
        "cursor": "hand2",
        "width": 14,
        "height": 2,
        "bd": 0,
        "highlightthickness": 0,
    }

    btn_menu_style = {
        "font": ("Helvetica", 14, "bold"),
        "bg": "white",
        "fg": "#dc2626",
        "activebackground": "#991b1b",
        "activeforeground": "white",
        "relief": "flat",
        "cursor": "hand2",
        "width": 18,
        "height": 2,
        "bd": 0,
        "highlightthickness": 0,
    }
    Button(frame_alt, text="Kaydet", command=save_list, **btn_save_style).pack(side=LEFT, padx=20)
    Button(frame_alt, text="Sıfırla", command=sifirla, **btn_reset_style).pack(side=LEFT, padx=20)
    Button(frame_alt, text="Ana Menüye Dön", command=ana_menu, **btn_menu_style).pack(side=LEFT, padx=20)

def insertion_sort(liste):
    global siralanmis_liste  # Fonksiyon dışında tanımlı olan değişkeni kullan
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    siralanmis_liste = liste  # Global değişkene atıyoruz
    verileri_goster(liste, "Insertion Sort ile Sıralanan Veriler", orijinal_kaydet=False)
def bubble_sort(liste):
    global siralanmis_liste
    for i in range(len(liste)):
        for j in range(0, len(liste) - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    siralanmis_liste = liste
    verileri_goster(liste, "Bubble Sort ile Sıralanan Veriler", orijinal_kaydet=False)

def selection_sort(liste):
    global siralanmis_liste
    for i in range(len(liste)):
        min_idx = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    siralanmis_liste = liste
    verileri_goster(liste, "Selection Sort ile Sıralanan Veriler", orijinal_kaydet=False)
def heapify(liste, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and liste[left] > liste[largest]:
        largest = left
    if right < n and liste[right] > liste[largest]:
        largest = right
    if largest != i:
        liste[i], liste[largest] = liste[largest], liste[i]
        heapify(liste, n, largest)

def heap_sort(liste):
    global siralanmis_liste
    n = len(liste)
    for i in range(n // 2 - 1, -1, -1):
        heapify(liste, n, i)
    for i in range(n - 1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i]
        heapify(liste, i, 0)
    siralanmis_liste = liste
    verileri_goster(liste, "Heap Sort ile Sıralanan Veriler", orijinal_kaydet=False)

def counting_sort(liste, exp):
    n = len(liste)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (liste[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (liste[i] // exp) % 10
        output[count[index] - 1] = liste[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        liste[i] = output[i]

def radix_sort(liste):
    global siralanmis_liste
    if not liste:
        messagebox.showerror("Hata", "Liste boş, sıralama yapılamaz.")
        return

    max_num = max(liste)
    exp = 1
    while max_num // exp > 0:
        counting_sort(liste, exp)
        exp *= 10
    siralanmis_liste = liste
    verileri_goster(liste, "Radix Sort ile Sıralanan Veriler", orijinal_kaydet=False)
def counting_sort_wrapper(liste):
    global siralanmis_liste
    if not liste:
        messagebox.showerror("Hata", "Liste boş, sıralama yapılamaz.")
        return
    max_val = max(liste)
    count = [0] * (max_val + 1)

    for num in liste:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            liste[index] = i
            index += 1
            count[i] -= 1
    siralanmis_liste = liste
    verileri_goster(liste, "Counting Sort ile Sıralanan Veriler", orijinal_kaydet=False)
def sifirla():
    # Orijinal listeyi tekrar göster
    verileri_goster(orijinal_liste, "Sıralama Sıfırlandı - Orijinal Veriler", orijinal_kaydet=False)

ana_menu()
form.mainloop()
