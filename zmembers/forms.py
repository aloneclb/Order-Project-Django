from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username', 
        'autofocus':''
    }))

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        """
            Username Yerine Mail Kullanma 
        """
        if '@' in username:
            try:
                user = User.objects.get(email = username)
            except:
                raise forms.ValidationError("Lütfen username veya email'inizi kontrol ediniz...")
            return user.username

        return username


class RegisterForm(UserCreationForm):
    # User Creation Form'un __init__ fonksiyonunu override ettim
    # Sayfa açıldığında istediğimiz field'sa otomatik focus yapmak için.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = False

    first_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name', 
        'autofocus':''
    })) # Böylece widget yapısı ile autofocus'ta ekleyebilirim

    last_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name', 
    }))

    username = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username', 
    }))

    email = forms.CharField(widget = forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'E-mail', 
    }))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
    }))

    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Re-Type Password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        """
            E-maili unique yapma
        """
        if User.objects.filter(email = self.cleaned_data['email']).exists():
             raise forms.ValidationError("Bu e-mail var lütfen başka bir e-mail kullanınız...")
        
        return self.cleaned_data['email']



class EditeProfileForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
    }))

    first_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
    }))

    last_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
    }))

    email = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
    }))


    


class PasswordChangeFormEdited(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))




