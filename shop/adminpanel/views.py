from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import redirect

from adminpanel.forms import *
from adminpanel.models import *

def index(request):
    return render(request, 'pages_list.html')

def products_list(request):
    products = {'products': Product.objects.all()}
    return render(request, 'products_list.html', products)

def product_create(request):
    if request.method == 'POST':
        product = Product.objects.create(shop=Shop.objects.first())
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.amount = request.POST['amount']
        product.price = request.POST['price']
        product.active = bool(request.POST['active'])
        if request.POST.getlist('categories'):
            product.categories.clear()
            for key in request.POST.getlist('categories'):
                product.categories.add(Category.objects.get(id=key))
        product.save()
        # обновление фотографий (обновляются только вновь загруженные вместо уже существующих)
        for i, file in enumerate(request.FILES):
            if f'image_{i}' in request.FILES:
                image = ProductImage.objects.create(product=product)
                image.images = request.FILES[f'image_{i}']
                image.save()
        return redirect('show_product')
    form = ProductForm(instance=None)
    return render(request, 'products_form.html', {'form': form})

def product_update(request, id):
    product = Product.objects.get(id=id)
    images = ProductImage.objects.filter(product=product)
    instance = {
        'product': product,
        'images': images
    }
    if request.method == 'POST':
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.amount = request.POST['amount']
        product.price = request.POST['price']
        product.active = bool(request.POST['active'])
        if request.POST.getlist('categories'):
            product.categories.clear()
            for key in request.POST.getlist('categories'):
                product.categories.add(Category.objects.get(id=key))
        product.save()
        # обновление фотографий (обновляются только вновь загруженные вместо уже существующих)
        for i, p_i in enumerate(images):
            if f'image_{i}' in request.FILES:
                p_i.images = request.FILES[f'image_{i}']
                p_i.save()
        return redirect('show_product')
    form = ProductForm(instance=instance)
    return render(request, 'products_form.html', {'form': form})

def product_delete(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('show_product')


def categories_list(request):
    categories = {'categories': Category.objects.all()}
    return render(request, 'category_list.html', categories)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_category')
    form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('show_category')
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('show_category')


def shops_list(request):
    shops = {'shops': Shop.objects.all()}
    return render(request, 'shop_list.html', shops)

def shop_create(request):
    if request.method == 'POST':
        shop = Shop.objects.create()
        shop.title = request.POST['title']
        shop.description = request.POST['description']
        shop.imageUrl = request.FILES['imageUrl']
        shop.save()
        return redirect('show_shop')
    form = ShopForm()
    return render(request, 'shop_form.html', {'form': form})

def shop_update(request, id):
    shop = get_object_or_404(Shop, pk=id)
    form = ShopForm(request.POST or None, instance=shop)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('show_shop')
    return render(request, 'shop_form.html', {'form': form})

def shop_delete(request, id):
    Shop.objects.filter(id=id).delete()
    return redirect('show_shop')
