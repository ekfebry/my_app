from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Beranda, Produk

def login(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())

def beranda(request):
  data = Beranda.objects.all()
  template = loader.get_template('beranda.html')
  context ={
    'menu': 'Macam-Macam Jenis Sablon yang Tersedia di Eka Sablon',
    'beranda' : data
  }
  return HttpResponse(template.render(context, request))

def produk(request):
  data = Produk.objects.all()
  template = loader.get_template('produk.html')
  context = {
    'list': 'Macam-Macam Produk dan Deskripsi :',
    'produk' : data
  }
  return HttpResponse(template.render(context, request))