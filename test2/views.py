from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Community_post
from .forms import Community_PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import Signup_form, Login_form
from django.contrib.auth import login, authenticate

from django.http import HttpResponse

from .models import Member_info
from .models import My_role, My_under
from .models import Post

from .forms import Member_info_form
from .forms import Post_form

####################################################################


def home(request):
    users = User.objects.all()
    posts = Post.objects.all()
    follows = []
    for x in posts:
        if x.identity.username == request.user.username:
            break
    




def home(request):
    posts = Post.objects.all()
    return render(request, 'test2/home.html', {'posts': posts})



"""
def home(request):
    if request.user.is_authenticated:
        #real_posts = []
        xx = My_role.objects.filter(identity=request.user.username)
        return HttpResponse(xx)
"""




"""
def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
        my_role = My_role.objects.filter(identity = request.user.username)
        real_posts = []

        y = []

        for x in My_role.objects.all():
            if x.identity == request.user.username:
                y = x.my_roles
                return HttpResponse(y)
        for x in y:
            for xx in posts:
                if x.identity == xx.identity:
                    real_posts.append(xx)
        return render(request, 'test2/home.html', {'posts:': real_posts})
    return HttpResponse('잘못된 접근입니다.')
"""



"""
def home(request):
    if request.user.is_authenticated:
        for x in My_role.objects.all():
            if request.user.username == x.identity:
                y = x.my_roles.all()
                break
        for x



        posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
        real_posts = []
        y = []
        for x in My_role.objects.all():
            if request.user.username == x.identity:
                y = x.my_roles.all()
                break
        for x in y:
            for xx in posts:
                if x.identity == xx.identity:
                    real_posts.append(xx)
        return render(request, 'test2/home.html', {'posts:': real_posts})
    return HttpResponse('잘못된 접근입니다.')
"""
#################################################

def signup(request):
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            #new_user = User.objects.create_user(form.username, form.email, form.password)
            #new_user = User.objects.create_user(**form.cleaned_data)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User.objects.create_user(username, email, password)
            new_user.save
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('member_info')
    else:
        form = Signup_form()
    return render(request, 'test2/signup.html', {'form':form})


def member_info(request):
    if request.method == "POST":
        form = Member_info_form(request.POST)
        if form.is_valid():
            mem = form.save(commit=False)
            mem.identity = request.user.username
            mem.name = form.cleaned_data['name']
            mem.myinfo = form.cleaned_data['myinfo']
            #mem.callnumber = form.cleaned_data['callnumber']
            mem.created_date = timezone.now()
            mem.save()
            return render(request, 'test2/home.html', {})
    else:
        form = Member_info_form()
    return render(request, 'test2/Member_info.html', {'form': form})



def Login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패')
    else:
        form = Login_form()
        return render(request, 'test2/login.html', {'form': form})



def post_new(request):
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.identity = request.user
            post.created_date = timezone.now()
            post.save()
            #new = form.save(commit=False)
            #new.user = request.user
            #new.save()
            return redirect('home')
    else:
        form = Post_form()
        return render(request, 'test2/post_new.html', {'form': form})













#######################################

def enter_sadari(request):
    return render(request, 'test2/sadari.html', {})

def enter_community(request):
    posts = Community_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'test2/community.html', {'posts': posts})

def community_post_detail(request, pk):
    post = get_object_or_404(Community_post, pk=pk)
    return render(request, 'test2/community_post_detail.html', {'post': post})

def community_post_new(request):
    if request.method == "POST":
        form = Community_PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('community_post_detail', pk=post.pk)
    else:
        form = Community_PostForm()
    return render(request, 'test2/community_post_new.html', {'form':form})

def community_post_edit(request, pk):
    post = get_object_or_404(Community_post, pk=pk)
    if request.method == "POST":
        form = Community_PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('community_post_detail', pk=post.pk)
    else:
        form = Community_PostForm(instance=post)
    return render(request, 'test2/community_post_new.html', {'form': form})
