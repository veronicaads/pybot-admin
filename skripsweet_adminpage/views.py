from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import *

def index(request):
    return HttpResponse(render(request, 'form.html', None))

def process_form(request):
    data = request.POST.copy()
    th = TransactionHeader()
    th.idtransaction = str(int(TransactionHeader.objects.annotate(Count('idtransaction'))) + 1)
    th.nohp = data.get('telp')
    th.namacust = data.get('nama')
    id = data.get('id[]')
    kuantitas = data.get('kuantitas[]')
    gambar = data.get('gambar[]')
    keterangan = data.get('keterangan[]')
    totalharga = 0
    for i in range(len(id)):
        od = OrderDetails()
        od.idorder = str(int(OrderDetails.objects.annotate(Count('idorder'))) + 1)
        od.idproduk = Produk.objects.find(pk=id[i])
        od.qty = int(kuantitas[i])
        od.gambar = gambar[i]
        od.keterangan = keterangan[i]
        od.save()
        totalharga += od.idproduk.harga * od.qty
    th.totalharga = 0
    th.alamatkirim = data.get('alamat')
    th.noresi = None
    th.ongkoskirim = 20000
    th.keterangantambahan = "-"
    th.idadmin = Admin.objects.first()
    th.idlogistik = Logistik.objects.first()
    th.save()
    th.totalharga = totalharga
    th.save()
    return HttpResponse(str(data))

