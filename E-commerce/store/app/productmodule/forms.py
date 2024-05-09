from django import forms
from .models import customers, products

class customersForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['f_name','l_name','phone','username','email','password']
        
    f_name = forms.CharField(max_length=20)
    l_name = forms.CharField(max_length=20)
    
    phone = forms.IntegerField()
    
    username = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 20)
    
class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['id','p_name','company','p_count','img_num']
        
    id = forms.IntegerField(required = True)
    p_name = forms.CharField(max_length=20)
    company = forms.CharField(max_length=20)
    
    p_count = forms.IntegerField()
    img_num = forms.IntegerField()
   

