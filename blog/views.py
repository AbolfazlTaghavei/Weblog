from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy

from . import models
from . import forms

class PostListView(generic.ListView):
    context_object_name = 'posts_list'
    template_name = 'blog/posts_list.html'

    def get_queryset(self):
        return models.Post.objects.filter(status='P').order_by('-datetime_modified')

class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def post_create_view(request):
#     if request.method == 'POST':
#         form = forms.NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = forms.NewPostForm()


#     return render(request, 'blog/post_create.html', {'form': form})

class PosrCreateView(generic.CreateView):
    form_class = forms.PostForm
    template_name = 'blog/post_create.html'
    


# def post_update_view(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#     form = forms.NewPostForm(request.POST or None, instance=post)

#     if form.is_valid():
#         form.save() 
#         return redirect('posts_list')

#     return render(request, 'blog/post_update.html', {'form': form})

class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm # or fields = ['', '', '']
    template_name = 'blog/post_update.html'

# def post_delete_view(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)

#     if request.method == "POST":
#         post.delete()
#         return redirect('posts_list')
    
#     return render(request, 'blog/post_delete.html', {'post': post, })

class PostDeleteView(generic.DeleteView):
    model = models.Post
    template_name = 'blog/post_delete.html'
    # get_success_url or this trick 
    # success_url = reverse_lazy('posts_list')

    def get_success_url(self):
        return reverse('posts_list')
