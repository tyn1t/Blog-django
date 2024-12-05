from django.contrib.auth.models import User
 
from django.db import models

from django.urls import reverse
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    auto = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    update_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)
   
    
    def __str__(self):
        return self.title 
    
    def get_aget_absolute_url(self):
        return reverse("blog_form", kwargs={'slug':self.slug})
    
    class Meta: 
        ordering = ['create_at']
        
