from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from ..models import Product
from ..forms import ReviewForm

def product_list(request):
    product_list = Product.objects.order_by('id')
    context = {'product_list': product_list}
    return render(request, 'vapeasy/product_list.html', context)

def product_datail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'vapeasy/product_detail.html', context)
