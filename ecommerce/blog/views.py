from django.shortcuts import render,get_object_or_404,reverse,redirect
from .models import Post
from .froms import CreatePostForm, PostEditForm

# Create your views here.




def PostList(request):
    postlist = Post.objects.all()
    context = {
        "postlist":postlist
    }
    template_name = "postlist.html"
    return render(request,template_name,context)




def PostDetail(request,id):
    post = get_object_or_404(Post,id=id)
    context = {
        'post':post
    }
    template_name = "postdetail.html"
    return render(request,template_name,context)


def PostUpdateis(request,id):
    post = get_object_or_404(Post,id=id)
    if request.user != post.Author :
        return redirect("home")
    else :
        if request.method == "POST" :
            form = PostEditForm(request.POST ,instance=post)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = PostEditForm(instance=post)
    return render(request,"update-post.html",context={"form":form})

def CreatPost(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST or None)
        if form.is_valid():
            new_post= form.save(commit=False)
            new_post.Author = request.user
            new_post.save()
            return redirect("home")
    else:
        form = CreatePostForm()
    context = {"form":form }
    template_name="CreatePostForm.html"
    return render(request,template_name,context)




