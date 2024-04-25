from django.shortcuts import render
from app.models.models import add_product

def home(request):
    return render(request, 'usermodule/home.html', {'product': __getproduct()})

def login(request):
    return render(request, 'usermodule/login.html')

def signup(request):
    return render(request, 'usermodule/signup.html')

def addproduct(request):
    if request.method == "POST":
        # between the () is the name from the request form
        id = request.POST.get('p_id')
        p_name = request.POST.get('p_name')
        c_name = request.POST.get('c_name')
        count = request.POST.get('count')
        img_num = request.POST.get('img_num')
        # the first name from the model the secound name from the varibles :ex 'company' from the model and 'c_name' from above 
        product = add_product(id = id, p_name = p_name, company = c_name, p_count = count, img_num = img_num)
        product.save()
        
    return render(request, 'usermodule/addProduct.html')

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
        {'id':1, 'pname':'Iphone 15', 'company':'Apple', 'img': ''},
        {'id':2, 'pname':'Galaxy S24 ultra', 'company':'Samsong', 'img': ''},
        {'id':3, 'pname':'Ipad Air 5', 'company':'Apple', 'img': ''},
    ]
    return products