from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, Systemunit, Accessories, Noteboo, Open, Promocod, Notepr


# Create your views here.
def index(request):
    products = Noteboo.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'shop/index.html', context)

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


class PromocodCreate(CreateView):
    model = Promocod
    fields = ['promo']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

def notepr(request):
    categories = Noteboo.objects.all()
    return render(request,'shop/notepr.html',{'categories': categories})

def notesale10(request):
    sale10 = Noteboo.objects.all()
    return render(request,'shop/notesale10.html',{'sale10': sale10})

def accsesor(request):
    accses = Accessories.objects.all()
    return render(request,'shop/accsesor.html',{'accses': accses})

def open(request, product_id):
    openings = Noteboo.objects.filter(product_id)
    return render(request,'shop/open.html',{'openings': openings})