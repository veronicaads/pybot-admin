from django.db import models

# ---------------------------------------------------------
# -------------------- Skema Transaksi --------------------
# ---------------------------------------------------------

class Admin(models.Model):
    idadmin = models.CharField(max_length=5, primary_key=True)
    namaadmin = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Produk(models.Model):
    idproduk = models.IntegerField(primary_key=True)
    merkhp = models.CharField(max_length=50)
    tipehp = models.CharField(max_length=50)
    material_hp = models.CharField(max_length=50)
    stock = models.IntegerField()
    harga = models.IntegerField()
    lama_pengerjaan = models.IntegerField()

class Logistik(models.Model):
    idlogistik = models.CharField(max_length=5, primary_key=True)
    namalogistik = models.CharField(max_length=50)

class Bank(models.Model):
    idbank = models.CharField(max_length=5, primary_key=True)
    namabank = models.CharField(max_length=50)
    norek = models.CharField(max_length=50)
    atasnama = models.CharField(max_length=50)

class TransactionHeader(models.Model):
    idtransaction = models.CharField(max_length=5, primary_key=True)
    idlogistik = models.ForeignKey(Logistik, on_delete=models.CASCADE)
    idadmin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    nohp = models.CharField(max_length=50)
    namacust = models.CharField(max_length=50)
    totalharga = models.IntegerField()
    alamatkirim = models.CharField(max_length=50)
    noresi = models.CharField(max_length=50, blank=True)
    ongkoskirim = models.IntegerField()
    keterangantambahan = models.TextField(blank=True)

class OrderDetails(models.Model):
    idorder = models.CharField(max_length=5, primary_key=True)
    idtransaction = models.ForeignKey(TransactionHeader, on_delete=models.CASCADE)
    idproduk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    qty = models.IntegerField()
    keterangan = models.TextField()
    gambar = models.FileField()

class BuktiTransfer(models.Model):
    idtransfer = models.CharField(max_length=5, primary_key=True)
    idtransaction = models.ForeignKey(TransactionHeader, on_delete=models.CASCADE)
    idbank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    total_transfer = models.IntegerField()
    gambar = models.FileField()

class InfoShop(models.Model):
    idshop = models.CharField(max_length=5, primary_key=True)
    namashop = models.CharField(max_length=50, blank=True)
    provinsi = models.CharField(max_length=50, blank=True)
    kota = models.CharField(max_length=50, blank=True)
    notlp = models.CharField(max_length=50, blank=True)

# ---------------------------------------------------------
# --------------------- Skema History ---------------------
# ---------------------------------------------------------

class Chat(models.Model):
    idchat = models.CharField(max_length=50, primary_key=True)
    message = models.TextField()
    timestamp = models.DateTimeField()
    status = models.BooleanField()

class Chatroom(models.Model):
    idchatroom = models.CharField(max_length=50, primary_key=True)
    profilename = models.CharField(max_length=50)

class ChatHistory(models.Model):
    idchat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    idchatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
