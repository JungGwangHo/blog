from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
from django.views.generic import View
#회원가입
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm
# ajax
from django.http import JsonResponse
def postList(request):
    posts = Post.objects.all()
    return render(request, 'blog/postList.html', {'posts': posts})

def readPost(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/readpost.html', {'post': post})

def editPost(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('myblog.views.readPost', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editPost.html', {'form': form})


class WritePostView(View):
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('myblog.views.readPost', id=post.id)
        # return redirect(request, 'blog/editPost.html', {'form': form})
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/editPost.html', {'form': form})

def signup(request):
    """signsup
    to register users
    """
    if request.method == "POST":
        userform = RegisterForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                reverse("signup_ok")
            )

    elif request.method =="GET":
        userform = RegisterForm()

    return render(request, "registration/signup.html", {"userform": userform,})

class DuplicationCheck(View):
    def post(self, request):
        # user = get_object_or_404(User, username=username)
        username = request.POST.get('username', None)
        data = {
            'is_taken': User.objects.filter(username__iexact=username).exists()
            }
        return JsonResponse(data)
