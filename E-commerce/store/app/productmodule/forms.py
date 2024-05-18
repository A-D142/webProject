from django import forms
from .models import customers, products

class customersForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['f_name','l_name','phone','username','email','password']
        
    f_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    l_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    
    phone = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'addproduct-input'}))
    
    username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    email = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    password = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    
class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['id','p_name','company','p_count','price']
        
    id = forms.IntegerField(required = True, widget=forms.NumberInput(attrs={'class': 'addproduct-input'}))
    p_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'addproduct-input'}), max_length=20)
    company = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'addproduct-input'}))
    
    p_count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'addproduct-input'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'addproduct-input'}))
   

