from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.auth import admin_only


# Create your views here.
@login_required
@admin_only
# def test(request):
#     return HttpResponse("This is rendered from the app.")

# def me(request):
#     return HttpResponse("this is rendered by suhana from the app.")

@login_required
@admin_only
def index(request):
    #fetch data from the table
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'products/products.html',context)

@login_required
@admin_only
def post_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product added successfully.')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'failed to add product.')
            return render(request,'/products/addproduct.html',{'form':form})
    context={
        'form':ProductForm
    }
    return render(request,'products/addproduct.html',context)

@login_required
@admin_only
def update_product(request,product_id):
    instance=Product.objects.get(id=product_id)

    if request.method=="POST":
        form=ProductForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product updated successfully.')
            return redirect('/products/')
        else:
            messages.add_message(request,messages.ERROR,'failed to update product.')
            return render(request,'/products/updateproduct.html',{'form':form})
    context={
        'form':ProductForm(instance=instance)
    }
    return render(request,'products/updateproduct.html',context)

@login_required
@admin_only
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Products deleted.')
    return redirect('/products')

@login_required
@admin_only
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category added successfully.')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'failed to add category.')
            return render(request,'products/addcategory.html',{'form':form})
    context={
        'form':CategoryForm
    }
    return render(request,'products/addcategory.html',context)

@login_required
@admin_only
def show_category(request):
    #fetch data from the table
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'products/category.html',context)

@login_required
@admin_only
def update_category(request,category_id):
    instance=Category.objects.get(id=category_id)

    if request.method=="POST":
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category updated successfully.')
            return redirect('/products/categories')
        else:
            messages.add_message(request,messages.ERROR,'failed to update category.')
            return render(request,'products/updatecategory.html',{'form':form})
    context={
        'form':CategoryForm(instance=instance)
    }
    return render(request,'products/updatecategory.html',context)

@login_required
@admin_only
def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Category deleted.')
    return redirect('/products/categories')
