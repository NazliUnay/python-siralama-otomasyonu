
# Sıralama Otomasyonu — Python & Tkinter Uygulaması

Python dili ve Tkinter GUI kütüphanesi kullanılarak geliştirilmiş, farklı yöntemlerle sayı listeleri oluşturup çeşitli sıralama algoritmalarıyla sıralamayı sağlayan masaüstü uygulamasıdır.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)
- [Özellikler](#özellikler)
- [Desteklenen Sıralama Algoritmaları](#desteklenen-sıralama-algoritmaları)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Kod Yapısı](#kod-yapısı)
- [Geliştirme ve Katkı](#geliştirme-ve-katkı)
- [Lisans](#lisans)

---

## Genel Bakış

Bu uygulama, farklı kaynaklardan sayı listesi oluşturmanıza olanak sağlar:

- Dışarıdan dosyadan okuma (metin dosyası şeklinde)
- Rastgele sayı üretme (kullanıcı tarafından belirlenen aralık ve adet)
- Kullanıcıdan elle giriş (virgülle ayrılmış sayı dizisi)

Oluşturulan liste ekranda gösterilir ve ardından 6 farklı algoritma ile sıralanabilir. Sıralama sonucu yine ekranda görüntülenir.

Kullanıcı dostu arayüzü ve tam ekran modu ile eğitim amaçlı, algoritmaların çalışma mantığını deneyimlemek için uygundur.

---

## Özellikler

- **Liste oluşturma:**
  - Dosyadan yükleme (her satırda bir sayı olacak şekilde)
  - Rastgele sayı listesi oluşturma (minimum, maksimum ve liste uzunluğu kullanıcı tarafından belirlenir)
  - Kullanıcıdan doğrudan sayı girişi (virgülle ayrılmış)

- **Sıralama algoritmaları:**
  - Insertion Sort
  - Bubble Sort
  - Selection Sort
  - Heap Sort
  - Radix Sort
  - Counting Sort

- **Arayüz:**
  - Tkinter tabanlı GUI
  - Tam ekran mod desteği
  - Listeyi ekranda okunabilir şekilde gösterme
  - Kullanıcı dostu menüler

---

## Desteklenen Sıralama Algoritmaları

### Insertion Sort  
Listeyi soldan sağa ilerleyerek, her elemanı doğru konumuna yerleştirir. Basit ve küçük listelerde etkilidir.

### Bubble Sort  
Yan yana olan elemanları karşılaştırıp, büyük olanı sağa “kabarcık” gibi taşır. Basit ama yavaş bir algoritmadır.

### Selection Sort  
Listedeki en küçük elemanı bulup sırayla başa yerleştirir. Karışıklığı azdır ama performansı düşük.

### Heap Sort  
Bir binary heap yapısı oluşturup, elemanları sıralar. Karmaşıklığı iyi, hızlıdır.

### Radix Sort  
Basamaklara göre elemanları sıralar. Sayılar pozitif ve belirli aralıktaysa oldukça hızlıdır.

### Counting Sort  
Sayıların sayısını sayarak sıralar. Sayı aralığı küçükse çok hızlıdır.

---

## Kurulum

1. **Python 3** sürümünün bilgisayarınızda kurulu olduğundan emin olun.  
   - İndirme: https://www.python.org/downloads/

2. **Tkinter** çoğu Python kurulumunda varsayılan gelir.  
   - Windows ve macOS genellikle hazırdır.  
   - Linux'ta `sudo apt-get install python3-tk` ile kurabilirsiniz.

3. Proje dosyalarını indirin veya klonlayın.

4. Komut satırından proje dizinine gidin.

5. Uygulamayı çalıştırmak için:

```bash
python sıralama_otomasyonu.py
```

---

## Kullanım

1. Uygulama açıldığında ana menü görüntülenir.

2. **Liste oluşturma seçenekleri**:
   - **Dosyadan Oku**: Sayıların bulunduğu metin dosyasını seçin. Dosya satır satır okunur.
   - **Rastgele Sayılar Oluştur**: Minimum, maksimum ve liste uzunluğunu girin.
   - **Kullanıcı Girişi**: Virgülle ayrılmış sayıları yazın (örn: 5,12,9,1).

3. Liste oluşturulduktan sonra ekranda gösterilir.

4. **Sıralama algoritmalarından birini seçin**. Seçilen algoritma listenizi sıralar ve sonucu gösterir.

5. İşlemi tekrarlamak veya yeni liste oluşturmak için ana menüye dönebilirsiniz.

---

## Kod Yapısı (Özet)

- `liste_olustur.py` (varsayılan olarak tüm fonksiyonlar aynı dosyada)
  - Dosya okuma fonksiyonu
  - Rastgele sayı oluşturma fonksiyonu
  - Kullanıcıdan liste alma fonksiyonu

- `siralama_algoritmalari.py`
  - Her sıralama algoritması ayrı fonksiyon olarak tanımlanmıştır.

- `arayuz.py`
  - Tkinter ile arayüz elemanlarının oluşturulması ve olay yönetimi.

---

## Geliştirme ve Katkı

- Kod yapısına modüler yapıda fonksiyonlar eklendi, genişletmeye uygundur.
- İstenirse dosyaya liste kaydetme, sıralama adımlarını görselleştirme, zaman ölçme gibi özellikler eklenebilir.
- Hatalar ve öneriler için iletişime geçebilirsiniz.

---

## Lisans

Bu proje MIT lisansı altında dağıtılmaktadır. İstediğiniz şekilde kullanabilir, değiştirebilir ve dağıtabilirsiniz.

---

## İletişim

- **Ad:** Şerife Nazlı Ünay  
- **E-posta:** [email@example.com]  
- **GitHub:** [github.com/kullaniciadi]

---

Teşekkürler!  
Projenizle iyi çalışmalar dilerim.
