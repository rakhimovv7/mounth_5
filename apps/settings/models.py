from django.db import models

# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/"
    )
    title = models.CharField(
        max_length=255,
        
    )
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

