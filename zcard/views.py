from django.shortcuts import render, redirect, get_object_or_404

from .models import Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


from zproduct.models import Product
from django.utils import timezone
from django.contrib.auth.decorators import login_required





@login_required(login_url='login')
def order_summary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'object': order
        }
        return render(request, 'zcard/order_summary.html', context)

    except ObjectDoesNotExist:
        messages.warning(request, "Aktif bir siparişiniz yok")
        return redirect("/")




@login_required(login_url='login')
def add_to_cart(request, barcode,slug):

    product = get_object_or_404(Product, barcode=barcode, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(
        item=product,
        user=request.user,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists(): # Kullanıcının Sepeti Var mı
        order = order_qs[0]

        if order.items.filter(item__slug=product.slug, item__barcode =product.barcode).exists(): # Eklenen Ürün Sepette Varmı
            
            if order_item.quantity < product.stock: # Eklenen Ürün Adedini Stok Karşılıyor mu
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "Bu ürün miktarı güncellendi.")
            
            else: # Eklenen Ürün Adedini Karşılamıyorsa    
                messages.info(request, "Bu üründen sepete daha fazla eklenemez.")
            return redirect("product:product_detail",slug, barcode)

        else: # Eklenen Ürün Sepette Yoksa Ekle
            order.items.add(order_item)
            messages.info(request, "Bu ürün sepetinize eklendi.")
            return redirect("product:product_detail",slug, barcode)

    else: # Kullanıcının Sepeti Yoksa Sepet Yarat Ve İtemi Ekle
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Ürün sepetinize eklendi.")
        return redirect("product:product_detail",slug, barcode)




@login_required(login_url='login')
def remove_to_cart(request, barcode,slug):
    product = get_object_or_404(Product, barcode=barcode, slug=slug) # Ürün    
    order_qs = Order.objects.filter(user=request.user, ordered=False) # Sepet

    if order_qs.exists(): # Kullanıcının Sepeti Var mı
        order = order_qs[0] # Sepet
        
        if order.items.filter(item__slug=product.slug).exists(): # Ters İlişki
            order_item = OrderItem.objects.filter(
                item=product,
                user=request.user,
            )[0]
            order_item.reduce_to_quantity()
            messages.info(request, "Ürün Miktarı Güncellendi...")
            return redirect('card:order_summary')

        else:
            messages.info(request, "Bu Ürün Sepetinizde Yok")
            return redirect("card:order_summary")

    else:
        messages.info(request, "Sepetiniz Yok")
        return redirect("card:order_summary")


@login_required(login_url='login')
def delete_to_cart(request, barcode,slug):
    product = get_object_or_404(Product, barcode=barcode, slug=slug) # Ürün    
    order_qs = Order.objects.filter(user=request.user, ordered=False) # Sepet

    if order_qs.exists(): # Kullanıcının Sepeti Var mı
        order = order_qs[0] # Sepet
        
        if order.items.filter(item__slug=product.slug).exists(): # Ters İlişki
            order_item = OrderItem.objects.filter(
                item=product,
                user=request.user,
            )[0]
            order_item.delete()
            messages.info(request, "Ürün Sepetten Silindi...")
            return redirect('card:order_summary')

        else:
            messages.info(request, "Bu Ürün Sepetinizde Yok")
            return redirect("card:order_summary")
            
    else:
        messages.info(request, "Sepetiniz Yok")
        return redirect("card:order_summary")



@login_required(login_url='login')
def checkout(request):
    context = dict()
    context['order'] = 'empty'

    order_qs = Order.objects.filter(user=request.user, ordered=False) # Sepet
    if order_qs.exists(): # Kullanıcının Sepeti Var mı
        order = order_qs[0] # Sepet
        context['order'] = order


    else:
        return redirect("card:order_summary")
    
    return render(request, 'zcard/checkout.html', context)