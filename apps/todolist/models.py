from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(default=False,verbose_name='Стаутс выполнения')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    
    def __str__(self) -> str:
        return self.title
    class Meta():
        verbose_name_plural = "Добавление задачи"