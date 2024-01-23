from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blogs/post_list.html',{'posts':posts})

@login_required
def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'blogs/post_detail.html',{'post':post})

@login_required
def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            # post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.id)
    else:
        form=PostForm()
    return render(request,'blogs/post_new.html',{'form':form})

@login_required
def post_edit(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            # post.published_date=timezone.now()
            form.save()
            return redirect('post_detail',pk=post.id)
    else:
        form=PostForm(instance=post)
    return render(request,'blogs/post_new.html',{'form':form})

@login_required
def post_draft(request):
    posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blogs/post_draft.html',{'posts':posts})

@login_required
def post_publish(request,pk):
    post=Post.objects.get(pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.id)

@login_required
def post_remove(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogs/add_comment_to_post.html', {'form': form})



@login_required
def comment_approve(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)