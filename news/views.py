from django.views.generic import ListView, DetailView
from .models import Post
from django.template.defaultfilters import date


class PostList(ListView):
    """ View for post list page """
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering = ['-data_create']
    paginate_by = 10



class PostDetail(DetailView):
    """ View for post detail page """
    model = Post
    template_name = 'one_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = date(self.object.data_create, "d.m.Y")
        return context


