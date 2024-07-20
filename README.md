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
    - [Sınıflar](#Sınıflar)
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

### Sınıflar



### `Item` Sınıfı
    ```python
    class Item:
      def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

      def __str__(self):
        return f"{self.name}: {self.quantity} adet, {self.price:.2f} TL"

-   **`Item` Sınıfı:** Envanterdeki her bir öğeyi temsil eder.
    -   **`__init__` Metodu:** Öğenin adını (`name`), miktarını (`quantity`) ve fiyatını (`price`) alır ve bu değerleri ilgili özelliklere (`attributes`) atar.
    -   **`__str__` Metodu:** Öğeyi, adı, miktarı ve fiyatıyla birlikte bir string olarak döner. Örneğin: "Kalem: 10 adet, 5.00 TL".

### `Inventory` Sınıfı

    ```python
    class Inventory:
      def __init__(self):
        self.items = {}

      def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, quantity, price)

      def update_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity = quantity
            self.items[name].price = price
        else:
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")

      def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")

      def list_items(self):
        items_str = "\n".join(str(item) for item in self.items.values())
        if items_str:
            messagebox.showinfo("Envanter", items_str)
        else:
            messagebox.showinfo("Envanter", "Envanter boş.")

-   **`Inventory` Sınıfı:** Envanterdeki öğeleri yönetir (ekleme, güncelleme, kaldırma ve listeleme).
    -   **`__init__` Metodu:** Envanterdeki öğeleri saklamak için bir sözlük (`self.items`) oluşturur.
    -   **`add_item` Metodu:** Yeni bir öğe ekler veya var olan bir öğenin miktarını artırır.
    -   **`update_item` Metodu:** Var olan bir öğeyi günceller. Öğeyi bulamazsa bir hata mesajı gösterir.
    -   **`remove_item` Metodu:** Var olan bir öğeyi envanterden kaldırır. Öğeyi bulamazsa bir hata mesajı gösterir.
    -   **`list_items` Metodu:** Tüm öğeleri listeler ve bir mesaj kutusunda gösterir.

### `InventoryApp` Sınıfı
    ```python
    class InventoryApp:
      def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Envanter Yönetim Sistemi")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14))
        self.style.configure("TButton", font=("Helvetica", 12))

        self.name_label = ttk.Label(root, text="Öğe Adı")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.name_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="EW")

        self.quantity_label = ttk.Label(root, text="Miktar")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.quantity_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        self.price_label = ttk.Label(root, text="Fiyat")
        self.price_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.price_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.price_entry.grid(row=2, column=1, padx=10, pady=10, sticky="EW")

        self.add_button = ttk.Button(root, text="Öğe Ekle", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10, sticky="EW")

        self.update_button = ttk.Button(root, text="Öğe Güncelle", command=self.update_item)
        self.update_button.grid(row=3, column=1, padx=10, pady=10, sticky="EW")

        self.remove_button = ttk.Button(root, text="Öğe Kaldır", command=self.remove_item)
        self.remove_button.grid(row=4, column=0, padx=10, pady=10, sticky="EW")

        self.list_button = ttk.Button(root, text="Envanteri Listele", command=self.list_items)
        self.list_button.grid(row=4, column=1, padx=10, pady=10, sticky="EW")

       def resize_window(event):
            width = event.width
            height = event.height
            self.root.geometry(f"{width}x{height}")

        self.root.bind("<Configure>", resize_window)
        self.root.columnconfigure(1, weight=1)
        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        def add_item(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.add_item(name, quantity, price)
        messagebox.showinfo("Başarılı", f"{name} eklendi.")

      def update_item(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.update_item(name, quantity, price)
        messagebox.showinfo("Başarılı", f"{name} güncellendi.")

      def remove_item(self):
        name = self.name_entry.get()
        self.inventory.remove_item(name)
        messagebox.showinfo("Başarılı", f"{name} kaldırıldı.")

      def list_items(self):
        self.inventory.list_items()

-   **`InventoryApp` Sınıfı:** Tkinter kullanarak envanter yönetim sistemi için GUI oluşturur.
    -   **`__init__` Metodu:** Arayüz öğelerini (label, entry, button) oluşturur ve düzenler. Ayrıca pencere boyutunu dinamik olarak ayarlayan bir fonksiyon tanımlar.
    -   **`add_item` Metodu:** Kullanıcıdan alınan girişlerle bir öğe ekler.
    -   **`update_item` Metodu:** Kullanıcıdan alınan girişlerle bir öğeyi günceller.
    -   **`remove_item` Metodu:** Kullanıcıdan alınan girişle bir öğeyi kaldırır.
    -   **`list_items` Metodu:** Tüm öğeleri listeler ve bir mesaj kutusunda gösterir.

### Ana Program
    ```python
    if __name__ == "__main__":
      root = tk.Tk()
      app = InventoryApp(root)
      root.mainloop()

-   **Ana Program Bölümü:**
    -   `root` adlı Tkinter ana penceresi oluşturulur.
    -   `InventoryApp` sınıfından bir nesne (`app`) oluşturulur ve `root` ana penceresi bu sınıfa geçirilir.
    -   `root.mainloop()` fonksiyonu, Tkinter pencere döngüsünü başlatır ve arayüzün kullanıcı etkileşimlerine tepki vermesini sağlar.
      
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
