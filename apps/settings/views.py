from django.shortcuts import render, redirect

from .models import *
from apps.blog.models import News, Service
from apps.products.models import Category, Product
from apps.telegram_bot.views import get_text


# Create your views here.
def index(request):
    title_page = "Главная страница"
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all().order_by('?')
    category = Category.objects.latest('id')
    service = Service.objects.latest('id')

    services = Service.objects.all().order_by('?')
    footer_categories = Category.objects.all().order_by('?')[:6]
    news = News.objects.all().order_by('?')
    
    products = Product.objects.all().order_by('?')
    popular = Product.objects.filter(popular=True).order_by('?')[:3]
    product_day = Product.objects.filter(product_day=True)[:1]
    featured = Product.objects.filter(featured=True).order_by('?')[:3]
    return render(request, "base/index.html",locals())

def about(request):
    title_page = "О нас"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    best_products = Product.objects.all().order_by('?')
    footer_categories = Category.objects.all().order_by('?')[:6]
    data = Data.objects.latest('id')
    teams = Team.objects.all().order_by('?')
    return render(request, "base/about.html",locals())

def contact(request):
    title_page = "Контакты"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')[:6]
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cause = request.POST.get('cause')
        Contact.objects.create(name=name, phone=phone, message=message, cause=cause)

        get_text(f""" Оставлен отзыв 
                Имя пользователя: {name}
                Номер телефона: {phone}
                Причина: {cause}
                Сообщение: {message}
                """)
        return redirect('index')

    return render(request, "base/contact.html", locals())

def faqs(request):
    title_page = "FAQ"
    settings = Settings.objects.latest('id')
    faqs = FAQs.objects.all()
    return render(request, 'base/faqs.html', locals())