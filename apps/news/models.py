from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(
    max_length=255,
    verbose_name="Заголовок"
    )
    description = models.CharField(
    max_length=255,
    verbose_name="описание"
    )
    photo = models.ImageField(
    upload_to='news',
    verbose_name="фото"
    )
    create_data = models.DateTimeField(
    auto_now_add = True,
    verbose_name="Дата новостей"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        
        verbose_name_plural = "Настройка новостей"
        