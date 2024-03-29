from django.shortcuts import render

def home(request):
    return render(request, 'usermodule/home.html', {'product': __getproduct()})

def login(request):
    return render(request, 'usermodule/login.html')

def product(request, id):
    products = __getproduct()
    product = None
    for p in products:
        if p['id'] == id:
            product = p
    context = {'product':product}    
    return render(request, 'usermodule/product.html', context)

def __getproduct():
    products = [
        {'id':1, 'pname':'Iphone 15', 'company':'Apple'},
        {'id':2, 'pname':'Galaxy S24 ultra', 'company':'Samsong'},
        {'id':3, 'pname':'Ipad Air 5', 'company':'Apple'},
    ]
    return products