from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product_Section, Product, Questions, Users
from .forms import CreateNewUser

# Create your views here.
def index(request):
    title = 'Underground-Dev'
    sections = Product_Section.objects.all()
    return render(request, 'index.html', {'title':title, 'sections':sections})

@login_required
def sections(request):
    sections = Product_Section.objects.all()
    return render(request, 'sections.html', {'sections':sections})

@login_required
def products(request, id):
    section = get_object_or_404(Product_Section, id=id)
    products = Product.objects.filter(product_section_id=id)
    return render(request, 'products.html', {'products':products, 'section':section})

def help(request):
    questions = Questions.objects.all()
    return render(request, 'help.html', {'questions':questions})


"""""""""""""""""""SESION"""""""""""""""""""""""""
def login(request):
    pass

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'register_form': CreateNewUser()})
    if request.method == 'POST':
        Users.objects.create(user_name=request.POST['user_name'], user_email=request.POST['user_email'], user_password=request.POST['user_password'])
        messages.info(request, 'New user has been created successfully!')
    return redirect('login')

def logout(request):
    logout(request)
    return redirect('/')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def shoping(request):
    return render(request, 'shoping.html')