import tkinter as tk
from tkinter import messagebox, ttk

# Öğe sınıfı, envanterdeki her bir öğeyi temsil eder.
class Item:
    def __init__(self, name, quantity, price):
        self.name = name          # Öğe adı
        self.quantity = quantity  # Öğe miktarı
        self.price = price        # Öğe fiyatı

    def __str__(self):
        return f"{self.name}: {self.quantity} adet, {self.price:.2f} TL"

# Envanter sınıfı, öğelerin eklenmesi, güncellenmesi, kaldırılması ve listelenmesi gibi işlemleri yönetir.
class Inventory:
    def __init__(self):
        self.items = {}  # Öğelerin saklandığı sözlük

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity += quantity  # Eğer öğe zaten varsa miktarını arttır
        else:
            self.items[name] = Item(name, quantity, price)  # Yeni bir öğe oluştur ve envantere ekle

    def update_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity = quantity  # Öğenin miktarını güncelle
            self.items[name].price = price        # Öğenin fiyatını güncelle
        else:
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")  # Hata mesajı göster

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]  # Öğeyi envanterden kaldır
        else:
            messagebox.showerror("Hata", f"Item '{name}' envanterde bulunamadı.")  # Hata mesajı göster

    def list_items(self):
        items_str = "\n".join(str(item) for item in self.items.values())  # Tüm öğeleri stringe dönüştür
        if items_str:
            messagebox.showinfo("Envanter", items_str)  # Öğeleri göster
        else:
            messagebox.showinfo("Envanter", "Envanter boş.")  # Envantersiz olduğunu bildir

# Envanter Uygulama sınıfı, Tkinter kullanarak GUI arayüzünü oluşturur ve kullanıcı etkileşimlerini yönetir.
class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()  # Envanter nesnesi oluştur

        self.root = root
        self.root.title("Envanter Yönetim Sistemi")  # Pencere başlığı
        self.root.geometry("500x400")  # Pencere boyutu
        self.root.resizable(True, True)  # Pencerenin boyutunu değiştirilebilir yap

        self.style = ttk.Style()  # ttk stil nesnesi oluştur
        self.style.configure("TLabel", font=("Helvetica", 14))  # Etiketlerin fontunu ayarla
        self.style.configure("TButton", font=("Helvetica", 12))  # Düğmelerin fontunu ayarla

        # Öğe Adı etiketi ve giriş alanı
        self.name_label = ttk.Label(root, text="Öğe Adı")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")  # Konum ve ayarlar

        self.name_entry = ttk.Entry(root, font=("Helvetica", 14))  # Giriş alanı oluştur
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="EW")  # Konum ve ayarlar

        # Miktar etiketi ve giriş alanı
        self.quantity_label = ttk.Label(root, text="Miktar")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.quantity_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Fiyat etiketi ve giriş alanı
        self.price_label = ttk.Label(root, text="Fiyat")
        self.price_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        
        self.price_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.price_entry.grid(row=2, column=1, padx=10, pady=10, sticky="EW")

        # Öğe Ekle düğmesi
        self.add_button = ttk.Button(root, text="Öğe Ekle", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10, sticky="EW")

        # Öğe Güncelle düğmesi
        self.update_button = ttk.Button(root, text="Öğe Güncelle", command=self.update_item)
        self.update_button.grid(row=3, column=1, padx=10, pady=10, sticky="EW")

        # Öğe Kaldır düğmesi
        self.remove_button = ttk.Button(root, text="Öğe Kaldır", command=self.remove_item)
        self.remove_button.grid(row=4, column=0, padx=10, pady=10, sticky="EW")

        # Envanteri Listele düğmesi
        self.list_button = ttk.Button(root, text="Envanteri Listele", command=self.list_items)
        self.list_button.grid(row=4, column=1, padx=10, pady=10, sticky="EW")

        # Pencere boyutunu dinamik olarak değiştiren fonksiyon
        def resize_window(event):
            width = event.width
            height = event.height
            self.root.geometry(f"{width}x{height}")

        # Pencere boyutu değiştiğinde resize_window fonksiyonunu tetikler
        self.root.bind("<Configure>", resize_window)

        # Pencere genişletilebilirlik ayarları
        self.root.columnconfigure(1, weight=1)  # İkinci sütunun genişletilebilirliği
        for i in range(5):
            self.root.rowconfigure(i, weight=1)  # Her satırın genişletilebilirliği

    # Öğe Ekle fonksiyonu: Kullanıcı girdileriyle bir öğe ekler
    def add_item(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.add_item(name, quantity, price)  # Envantere öğe ekle
        messagebox.showinfo("Başarılı", f"{name} eklendi.")  # Bilgi iletişim kutusu göster

    # Öğe Güncelle fonksiyonu: Kullanıcı girdileriyle bir öğeyi günceller
    def update_item(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        self.inventory.update_item(name, quantity, price)  # Envanterdeki öğeyi güncelle
        messagebox.showinfo("Başarılı", f"{name} güncellendi.")  # Bilgi iletişim kutusu göster

    # Öğe Kaldır fonksiyonu: Kullanıcı girdisiyle bir öğeyi kaldırır
    def remove_item(self):
        name = self.name_entry.get()
        self.inventory.remove_item(name)  # Envanterden öğe kaldır
        messagebox.showinfo("Başarılı", f"{name} kaldırıldı.")  # Bilgi iletişim kutusu göster

    # Envanteri Listele fonksiyonu: Tüm envanter öğelerini listeler
    def list_items(self):
        self.inventory.list_items()  # Envanteri listele

# Ana program bölümü
if __name__ == "__main__":
    root = tk.Tk()  # Tkinter ana penceresi oluştur
    app = InventoryApp(root)  # InventoryApp sınıfını başlat
    root.mainloop()  # Pencere döngüsünü başlat
