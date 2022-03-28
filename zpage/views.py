from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Slider, AboutUs, Contact
from .forms import ContactForm

# Create your views here.


def index(request):
    context = dict()
    
    if request.path == '/':
        context['sliders'] = Slider.objects.all()
        return render(request, 'zpage/index.html', context)

    elif request.path == '/hakkimizda/':
        context['aboutus'] = AboutUs.objects.filter(status = 1).first()
        return render(request, 'zpage/hakkimizda.html', context)

    else:
        return render(request, 'zpage/index.html', context)



def contact(request):
    context = dict()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            Contact.objects.create(
                name = form.cleaned_data.get('name'),
                email = form.cleaned_data.get('email'),
                message = form.cleaned_data.get('message'),
                phone = form.cleaned_data.get('phone'),
                ip = request.META.get('REMOTE_ADDR') # İp adresini aldık 
            )
            messages.success(request, 'Mesajınız başarı ile gönderildi. Bizimle iletişime geçtiğiniz için teşekkür ederiz...')
            return redirect('contact')
        else:
            messages.warning(request, 'Mesajınız gönderilemedi. Lütfen tekrar deneyiniz...')
            return redirect('contact')

    else:
        context['form'] = ContactForm()     

    
    return render(request, 'zpage/iletisim.html', context)



