from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

# Create your views here.
def event1(request):
    return render(request, 'event1.html')

def event2(request):
    return render(request, 'event2.html')

def index(request):
    posts = Post.objects
    return render(request,'postslist.html',{'posts':posts})

def post_create(request):

    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
        return redirect('index')

    else:
        form = PostForm()
    return render(request,'postcreate.html', {'form':form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'postdetail.html', {'post' : post})

def post_update(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    form = PostForm(request.POST, instance = post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'postupdate.html', {'form':form})


def post_delete(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')
