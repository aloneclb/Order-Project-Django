from django.shortcuts import render, redirect
from .models import Product, Category, Wishlist
# Create your views here.
from django.db.models import Q



def product_list(request):
    context = dict()
    context['products'] = Product.objects.all()
    context['categories'] = Category.objects.all()

    return render(request, 'zproduct/product_list.html', context)

# TODO: iki fonksiyonu birleştir.


def category_list(request, slug):
    context = dict()
    context['products'] = Product.objects.filter(category__slug = slug)
    context['categories'] = Category.objects.all()
    return render(request, 'zproduct/product_list.html', context)


def product_search(request):
    """
        Sitedeki Search Alanı'na Girilen Değere Ait Ürünleri Listelemek İçin Yapılmıştır.
    """
    # if str(request.POST.get('search_query')) == '':
    #     print('girdi')
    # TODO: Boş gönderilmesine bak

    if request.method == 'POST':

        products = Product.objects.filter(
            Q(brand__icontains = str(request.POST.get('search_query'))) | 
            Q(title__icontains = str(request.POST.get('search_query')))
            )

        context = dict()
        context['products'] = products
        context['categories'] = Category.objects.all()
        context['search_data'] = str(request.POST.get('search_query'))
        
        return render(request, 'zproduct/product_list.html', context)

    else:
        return redirect('index')



def product_detail(request, slug, barcode):
    context = dict()
    context['product'] = Product.objects.get(slug=slug, barcode=barcode)
    return render(request, 'zproduct/product_detail.html', context)



# TODO : Bu formu dinamik gönder
def product_filter(request):
    if request.GET.get('gndr'): # Gender
        products = Product.objects.filter(gender__in = dict(request.GET)['gndr'])
        context = dict()
        context['products'] = products
    else:
        context = dict()

    context['categories'] = Category.objects.all()

    return render(request, 'zproduct/product_list.html', context)



def wishlist(request):
    pass
