from django.shortcuts import render, redirect

from .models import *
from apps.blog.models import News
from apps.products.models import Category, Product
from apps.telegram_bot.views import get_text


# Create your views here.
def index(request):
    title_page = "Главная страница"
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all().order_by('?')
    about = About.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    footer_categories = Category.objects.all().order_by('?')
    products = Product.objects.all().order_by('?')
    popular_products = Product.objects.all().order_by('?')[:8]
    featured_products = Product.objects.all().order_by('?')[:4]
    news = News.objects.all().order_by('?')[:6]
    all_products = Product.objects.all().order_by('?')
    return render(request, "base/index.html",locals())

def about(request):
    title_page = "О нас"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    best_products = Product.objects.all().order_by('?')
    footer_categories = Category.objects.all().order_by('?')
    data = Data.objects.latest('id')
    return render(request, "base/about.html",locals())

def contact(request):
    title_page = "Контакты"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    footer_categories = Category.objects.all().order_by('?')
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

def quiz(request):
    title_page = "Опросник"
    about = About.objects.latest('id')
    settings = Settings.objects.latest('id')
    if request.method =="POST":
       info =  request.POST.get('fullinfo').replace("quiz", "Вопрос №").split("|")
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       quiz_3 = request.POST.get('quiz_3')

       fullinfo = []
       for i in info:
           if len(i) > 1:
               fullinfo.append(i)
               print(i)
       print(fullinfo)
       print(len(fullinfo))

       fullinfo_pro = [i.strip() for i in info if len(i.strip()) > 1]
       formatted_fullinfo = '\n'.join(fullinfo_pro)
       get_text(
       f"""
Новая заявка:

Имя пользователя: {name}

Номер телефона: {phone}

На вопрос №3 (Какие проблемы возникают с вашим текущим ноутбуком?) ответил:
{quiz_3}

Выбранные поля:

{formatted_fullinfo}
        """
    )
       return redirect("index")
    return render(request, 'base/quiz.html', locals())