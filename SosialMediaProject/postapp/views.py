from django.shortcuts import render,redirect,get_object_or_404
from postapp.models import PostModel
from postapp.forms import PostForm,SignUpForm
from django.contrib.auth.decorators import login_required


def home_view(request):
    user_post=PostModel.objects.all()
    if request.POST:
        search_data=request.POST.get('search')
        user_post=user_post.filter(text__icontains=search_data)
        return render(request,'home.html',{"user_post":user_post})
    return render(request,'home.html',{"user_post":user_post})

@login_required
def create_post(request):
    msg=""
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home_view')
    else:
       form=PostForm()
       return render(request,'create_post.html',{"form":form})

@login_required 
def update_post(request,id):
    post=get_object_or_404(PostModel,pk=id,user=request.user)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home_view')
    form=PostForm(instance=post)
    return render(request,'create_post.html',{"form":form})

@login_required
def delete_post(request,id):
    post=PostModel.objects.get(id=id)
    if request.POST:
        post.delete()
        return redirect('home_view')
    return render(request,'delete.html')


def signup_view(request):
    if request.POST:
        form=SignUpForm(request.POST)
        user=form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    form=SignUpForm()
    return render(request,'signup.html',{"form":form})
