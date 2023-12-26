from django.http import HttpResponse
from django.template import loader

def login(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())

def beranda(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())

def produk(request):
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())