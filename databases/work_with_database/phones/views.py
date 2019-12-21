from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_opt = request.GET.get('sort')
    if not sort_opt:
        phone_list = Phone.objects.all()
    elif sort_opt == 'min_price':
        phone_list = Phone.objects.all().order_by('price')
    elif sort_opt == 'max_price':
        phone_list = Phone.objects.all().order_by('-price')
    elif sort_opt == 'name':
        phone_list = Phone.objects.all().order_by('name')
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all().get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
