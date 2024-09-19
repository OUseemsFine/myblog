from django.shortcuts import render

# Create your views here.
from .models import Blog, News

def index(request):
    '''index page'''
    news_list = News.objects.all().order_by('-update_date')
    context = {
        'news_list': news_list
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'
    
class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog'
    