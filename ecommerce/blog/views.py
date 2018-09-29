from django.shortcuts import render,get_object_or_404,reverse,redirect
from .models import Post
from .froms import CreatePostForm

# Create your views here.




def PostList(request):
    postlist = Post.objects.all()
    context = {
        "postlist":postlist
    }
    template_name = "postlist.html"
    return render(request,template_name,context)




def PostDetail(request,slug_post,id):
    post = get_object_or_404(Post,slug=slug_post)
    context = {
        'post':post
    }
    template_name = "postdetail.html"
    return render(request,template_name,context)



def CreatPost(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreatePostForm()
    context = {"form":form }
    template_name="CreatePostForm.html"
    return render(request,template_name,context)


