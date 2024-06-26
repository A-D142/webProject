from django.shortcuts import render, redirect
from .models import customers, products, carts
from .forms import customersForm, productsForm

def home(request):
    if request.method == 'POST':
        addtocart(request)
    product = products.objects.all()
    return render(request, 'productmodule/home.html', {'product': product})

def addtocart(request):
    pid = request.POST.get("dataproduct", "")
    obj = products.objects.get(id = pid)
    data = carts(p_name = obj.p_name, p_count = 1, price = obj.price, p_id = obj.id, p_img = obj.p_image)
    data.save()

def cart(request):
    if request.method == 'POST':
        pid = request.POST.get("dataproduct", "")
        obj = carts.objects.get(id = pid)
        obj.delete()
    obj = carts.objects.all()
    return render(request, 'productmodule/cart.html',{'product': obj})

def deletecart(request):
    obj = carts.objects.all()
    for o in obj:
        o.delete()
    return redirect('cart')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = customers.objects.get(username=username)
            if customer.password == password:
                # Passwords match, login successful
                print(f"Login successful for user: {customer.f_name}")
                return redirect('home')  # Redirect to another page
            else:
                # Passwords don't match
                print("Login not successful ")
                return redirect('login')
        except customers.DoesNotExist:
            return redirect('signup')
    form = customersForm(None)
    return render(request, 'productmodule/login.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = customersForm(request.POST)
        if form.is_valid:
            obj = form.save()
            return redirect('login')
    form = customersForm(None)
    return render(request, 'productmodule/signup.html', {'form':form})

def addproduct(request):
    if request.method == 'POST':
        form = productsForm(request.POST, request.FILES)
        if form.is_valid:
            obj = form.save()
            return redirect('addproduct')
    form = productsForm(None)        
    return render(request, 'productmodule/addProduct.html', {'form':form})

def product(request, id):
    if request.method == 'POST':
        addtocart(request)
        redirect('home')
    product = products.objects.get(id = id)    
    return render(request, 'productmodule/product.html', {'product':product})

def updateproduct(request, id):
    obj = products.objects.get(id = id)
    if request.method == 'POST':
        form = productsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj.save()git
            return redirect('product', id = obj.id)
    form = productsForm(instance=obj)        
    return render(request, 'productmodule/updateproduct.html', {'form':form})

def update(request):
    pid = request.POST.get("dataproduct", "")
    return redirect('updateproduct/'+pid)

def deleteproduct(request):
    if request.method == 'POST':
        pid = request.POST.get("dataproduct", "")
        obj = products.objects.get(id = pid)
        obj.delete()
    return redirect('home')