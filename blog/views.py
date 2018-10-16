from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


class PostView(ListView):
    model = Post
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetail(DetailView):
    model = Post


class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/details.html'
    model = Post
    form_class = PostForm

class PostUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/details.html'
    model = Post
    form_class = PostForm

class PostDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/details.html'
    model = Post
    success_url = reverse_lazy('blog:index')

class PostDraftList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/detail.html'
    model = Post
    context_object_name = 'post_drafts'
    template_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)

    else:
        form=CommentForm()
        return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:detail', pk=comment.post.pk)

@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:detail', pk=post_pk)
