from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    descriptions = RichTextField(
        verbose_name="Описание новости"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image_news/"
    )
    create = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок услуги"
    )
    descriptions = RichTextField(
        verbose_name="Описание услуги"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image_service/"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"