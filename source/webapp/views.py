from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from .models import PRODUCT_CATEGORY_CHOICES
from .forms import ProductForm, SearchForm


def index_view(request):
    products = Product.objects.filter(amount__gt=0).order_by('category','name')
    form = SearchForm()
    return render(request, 'index.html', context={
        'products': products,
        'form':form
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })

def product_create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {'statuses': PRODUCT_CATEGORY_CHOICES, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'update.html', context={'form': form, 'product': product})

    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.amount = form.cleaned_data['amount']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form})



def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')




def search(request):
    print(request.GET.get('name'))
    form = SearchForm(data=request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        products= Product.objects.filter(name__contains=name)
        return render(request, 'index.html', context={
        'products': products,
        'name':name,
        'form':form
    })