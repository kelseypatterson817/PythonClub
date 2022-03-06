from django.shortcuts import render
from .models import ProductType, Product, Review
from django.urls import reverse_lazy
from .forms import ProductForm
from django.contrib.auth.decorators import login_required'

# Create your views here.
def index (request):
    return render(request, 'techapp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'techapp/types.html' ,{'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'techapp/products.html', {'products_list': products_list})
    
def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'techapp/proddetails.html', context=context)

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'techapp/newproduct.html', {'form': form})

def loginmessage(request):
    return render(request, 'techapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'techapp/logoutmessage.html')

@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'techapp/newproduct.html', {'form': form})