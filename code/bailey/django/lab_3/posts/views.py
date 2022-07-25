from xml.etree.ElementTree import Comment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Comments, Post
from .forms import CommentForm

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-created')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self , **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comments.objects.filter(CommentPost=self.get_object())
        number_of_comments = connected_comments.count()
        data['comments'] = connected_comments
        data['no_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data
    
    def post(self , request , *args , **kwargs):
        if self.request.method == 'POST':
            print('Reached here')
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent=None

            

            new_comment = Comments(content=content , author = self.request.user , CommentPost=self.get_object() , parent=parent)
            new_comment.save()
            return redirect(self.request.path_info)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author




            
