from django import forms
from zpage.models.contact import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Yorumu gir...'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Emaili gir...'}),
            'message': forms.Textarea(attrs={'class':'form-control formtextareaozel',
                                             'placeholder':'Mesajınızı gir...' ,
                                             'resize':'none'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefonu gir...'}),            
        }