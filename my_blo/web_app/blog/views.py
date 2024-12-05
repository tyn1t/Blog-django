from django.forms import BaseModelForm
from django.views import generic
from django.http import HttpResponse, JsonResponse


# my db
from .models import Blog

class PostAPIView(generic.CreateView):
    model = Blog
    template_name= "blog/index.html"
    fields =  ['title', 'content', 'public', 'slug']
    
    
    def form_valid(self, form):
        self.object = form.save()
        
        return self.render_to_response(self.get_context_data(form=form))

class ListAPIView(generic.ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name= "blog/list_blog.html"
    queryset= Blog.objects.all()
    fields =  ['title', 'content', 'auto','create_at']
