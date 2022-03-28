from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages

# Parola Değişikliği için
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import (LoginForm, 
                    RegisterForm, 
                    EditeProfileForm, 
                    PasswordChangeFormEdited)





# Kimliksiz kullanıcı dekoratörü
def anonymous_required(function=None, redirect_url = None):
    """
        login_required same as
    """
    if not redirect_url:
        redirect_url = 'index'

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url= redirect_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
 


@anonymous_required
def login(request):
    if request.method == 'POST':# Eğer method Post İse
        form = LoginForm(request.POST) # formu belirle

        if form.is_valid():# Eğer form geçerli şekilde doldurulduysa
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username = username, password=password)

            if user is not None: # Eğer kullanıcı var ise

                if user.is_active: # Eğer kullanıcı var ve aktif ise
                    auth.login(request,user)
                    # Eğer Next Var İse
                    if request.GET.get('next') != None:
                        next_page = request.GET.get('next')
                        return redirect(next_page)
                    else:
                        messages.info(request, 'Hoşgeldiniz...')
                        return redirect('index')

                else: 
                    messages.info(request,'Disabled Account')
        
            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()
    
    return render(request, 'zmembers/login.html', {'form':form})




@anonymous_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hesabınız Başarı İle Oluşturuldu. Giriş Yapabilirsiniz...')
            return redirect('login')

    else:
        form = RegisterForm()
    
    return render(request, 'zmembers/register.html', {'form': form})





@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Başarı İle Çıkış Yapıldı')
    return redirect('index')





@login_required(login_url='login')
def change_password(request,id):    
    url_user = get_object_or_404(User,id = id)
    

    # Kullanıcıyı aldıysan mevcut kullanıcı ile karşılaştır aynı değilse kendi profiline yönlendir.
    if url_user.id != request.user.id:
        return redirect('profile')
    
    if request.method == 'POST':
        form = PasswordChangeFormEdited(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Formun Miras Aldığı Sınıfın Save Methodunu Çalıştırdık Bu şekilde O userin Şifresini Değiştirdik.
            # User modelinin set_password fonksiyonu ile 
            update_session_auth_hash(request, user)  # Important!
            # Şifre değiştirilince kullanıcının diğer oturumlardan çıkmasını sağlar.
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeFormEdited(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

