from django.shortcuts import render
#views connect models and templates
from .models import Post
#. means current directory
#post - name of model
from django.utils import timezone
def post_list(request):
#need to take models to display, pass them to template
    return render(request, 'blog/post_list.html', {'posts': posts})
    posts = Post.objects.filter(published_date__lte=timezone.now()).order)by('published_date')
#render - request =, template file, {} template use	