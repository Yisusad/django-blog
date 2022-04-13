from tabnanny import verbose
from django.db import models

#ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    title = models.CharField(max_length=200, verbose_name='Título')
    desc =  models.TextField(verbose_name='Descripción')
    conte = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True,
    verbose_name='Creacíon')
    updated = models.DateTimeField(auto_now=True,
    verbose_name='Editado')
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones' 
        ordering =['-created']
    
    def __str__(self):
        return self.title