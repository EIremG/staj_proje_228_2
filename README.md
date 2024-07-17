# staj_proje_228_2

--------------------------

# Envanter Yönetim Sistemi: Sistem Tasarımı ve Kullanım Talimatları

## İçindekiler
--------------------------

1. [Giriş](#giriş)
2. [Sistem Tasarımı](#sistem-tasarımı)
    - [Mimari](#mimari)
    - [Veri Modeli](#veri-modeli)
    - [Kullanıcı Arayüzü](#kullanıcı-arayüzü)
3. [Kullanım Talimatları](#kullanım-talimatları)
    - [Sistemin Başlatılması](#sistemin-başlatılması)
    - [Öğe Ekleme](#öğe-ekleme)
    - [Öğe Güncelleme](#öğe-güncelleme)
    - [Öğe Kaldırma](#öğe-kaldırma)
    - [Envanteri Listeleme](#envanteri-listeleme)
4. [Sonuç](#sonuç)


## Giriş
--------------------------


Bu belge, Python ile geliştirilmiş bir Envanter Yönetim Sistemi'nin sistem tasarımını ve kullanım talimatlarını açıklamaktadır. Bu sistem, kullanıcıların envanterdeki öğeleri eklemelerine, güncellemelerine, kaldırmalarına ve listelemelerine olanak tanıyan basit bir grafik kullanıcı arayüzü (GUI) sağlar.

## Sistem Tasarımı
--------------------------


### Mimari

Sistem, iki ana bileşenden oluşmaktadır:

1. **Backend (Arka Uç)**: Envanter yönetimi işlemlerini gerçekleştiren `Item` ve `Inventory` sınıflarından oluşur.
2. **Frontend (Ön Uç)**: Tkinter kullanılarak oluşturulmuş GUI uygulaması olan `InventoryApp` sınıfından oluşur.

### Veri Modeli

- **Item**: Envanterdeki her bir öğeyi temsil eder. Aşağıdaki özelliklere sahiptir:
  - `name`: Öğenin adı.
  - `quantity`: Öğenin miktarı.
  - `price`: Öğenin fiyatı.
  
- **Inventory**: Envanteri yönetir ve öğeler üzerinde ekleme, güncelleme, kaldırma ve listeleme işlemlerini gerçekleştirir.

### Kullanıcı Arayüzü

Kullanıcı arayüzü, Tkinter kullanılarak oluşturulmuş olup, aşağıdaki bileşenleri içerir:

- **Etiketler ve Giriş Alanları**: Öğe adı, miktarı ve fiyatı için.
- **Düğmeler**: Öğe ekleme, güncelleme, kaldırma ve envanteri listeleme işlemleri için.
- **Mesaj Kutuları**: Kullanıcıya işlem sonuçlarını göstermek için.

## Kullanım Talimatları
--------------------------


### Sistemin Başlatılması

1. **Python Ortamı Hazırlama**:
   - Gerekli kütüphanelerin yüklü olduğundan emin olun:
     ```bash
     pip install tkinter
     ```

2. **Kodu Çalıştırma**:
   - `inventory_app.py` dosyasını PyCharm veya başka bir Python IDE'si kullanarak açın.
   - Dosyayı çalıştırarak GUI uygulamasını başlatın:
     ```python
     python inventory_app.py
     ```

### Öğe Ekleme

1. **Öğe Adı, Miktar ve Fiyat Girişi**:
   - `Öğe Adı` alanına eklemek istediğiniz öğenin adını yazın.
   - `Miktar` alanına eklemek istediğiniz miktarı girin.
   - `Fiyat` alanına öğenin fiyatını girin.

2. **Öğe Ekle Düğmesi**:
   - `Öğe Ekle` düğmesine tıklayın.
   - Başarılı ekleme işleminden sonra bir onay mesajı görünecektir.

### Öğe Güncelleme

1. **Öğe Adı, Miktar ve Fiyat Girişi**:
   - `Öğe Adı` alanına güncellemek istediğiniz öğenin adını yazın.
   - `Miktar` alanına yeni miktarı girin.
   - `Fiyat` alanına yeni fiyatı girin.

2. **Öğe Güncelle Düğmesi**:
   - `Öğe Güncelle` düğmesine tıklayın.
   - Başarılı güncelleme işleminden sonra bir onay mesajı görünecektir.

### Öğe Kaldırma

1. **Öğe Adı Girişi**:
   - `Öğe Adı` alanına kaldırmak istediğiniz öğenin adını yazın.

2. **Öğe Kaldır Düğmesi**:
   - `Öğe Kaldır` düğmesine tıklayın.
   - Başarılı kaldırma işleminden sonra bir onay mesajı görünecektir.

### Envanteri Listeleme

1. **Envanteri Listele Düğmesi**:
   - `Envanteri Listele` düğmesine tıklayın.
   - Envanterdeki tüm öğeler bir mesaj kutusunda listelenecektir.

## Sonuç
--------------------------


Bu belge, Envanter Yönetim Sistemi'nin sistem tasarımını ve kullanım talimatlarını detaylandırmaktadır. Kullanıcıların bu talimatları izleyerek sistemi verimli bir şekilde kullanmaları amaçlanmaktadır.
