from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import *

def index(request):
    prod = Produk.objects.all()
    return HttpResponse(render(request, 'form.html', prod))

def process_form(request):
    data = request.POST.copy()
    th = TransactionHeader()
    th.idtransaction = str(int(1 if TransactionHeader.objects.all().last() == None else TransactionHeader.objects.all().last().idtransaction) + 1)
    th.nohp = data.get('telp')
    th.namacust = data.get('nama')
    id = data.getlist('id[]')
    kuantitas = data.getlist('kuantitas[]')
    gambar = data.getlist('gambar[]')
    keterangan = data.getlist('keterangan[]')
    totalharga = 0
    th.totalharga = 0
    th.alamatkirim = data.get('alamat')
    th.noresi = None
    th.ongkoskirim = 20000
    th.keterangantambahan = "-"
    th.idadmin = Admin.objects.first()
    th.idlogistik = Logistik.objects.first()
    th.save()
    for i in range(len(id)):
        od = OrderDetails()
        od.idorder = str(int(1 if OrderDetails.objects.all().last() == None else OrderDetails.objects.all().last().idorder) + 1)
        od.idproduk = Produk.objects.get(pk=id[i])
        od.qty = int(kuantitas[i])
        od.gambar = gambar[i]
        od.keterangan = keterangan[i]
        od.idtransaction = th
        od.save()
        totalharga += od.idproduk.harga * od.qty
    th.totalharga = totalharga
    th.save()
    return HttpResponse(str(data))

