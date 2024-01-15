from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField


# Create your models here.
class Settings(models.Model):
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для фотографии"
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта "

class Slide(models.Model):
    title = RichTextField(
        verbose_name="Заголовок"
    )
    back_image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "bacground_image",
        verbose_name="Фотография для баннера",
        blank = True,null = True    
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "bacground_image",
        verbose_name="Фотография",
        blank = True,null = True
    )
    link = models.URLField(
        max_length=255,
        verbose_name='Ссылка',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

class About(models.Model):
    title = RichTextField(
        verbose_name="Заголовок"
    )
    descriptions = RichTextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография",
        blank = True,null = True    
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Data(models.Model):
    title_1 = RichTextField(
        verbose_name="Текст №1",
    )
    title_2 = RichTextField(
        verbose_name="Текст №2",
    )
    title_3 = RichTextField(
        verbose_name="Текст №3",
    )
    title_4 = RichTextField(
        verbose_name="Текст №4",
    )

    class Meta:
        verbose_name = "Наша статистика"
        verbose_name_plural = "Наша статистика"


class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True,blank=True
    )
    cause = models.CharField(
        max_length=155,
        verbose_name="Причина",
        null=True,blank=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = "Оставленные отзывы"

class Team(models.Model):
    name = RichTextField(
        verbose_name="ФИО"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография сотрудника",
        blank = True,null = True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона (whatsapp)'
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"

class FAQs(models.Model):
    question = models.CharField(
        max_length=155,
        verbose_name="Вопрос"
    )
    answer = models.TextField(
        verbose_name="Ответ"
    )

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"