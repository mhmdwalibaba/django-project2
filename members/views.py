from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from .forms import AccountForm
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    return HttpResponse('خوش امدیدی دوستان')
# def postlist(request):
#     posts=Post.objects.filter(status='published')
#     paginator=Paginator(posts,2)
#     page=request.GET.get('page')
#     try:
#        posts=paginator.page(page)
#     except PageNotAnInteger:
#        posts=paginator.page(1)
#     except:
#       posts=paginator.page(paginator.num_pages)
#
#     return render(request,'members/Post/list.html',{'posts': posts})
class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'members/Post/list.html'
def postdetail(request,post,pk):
    post=get_object_or_404(Post,slug=post,id=pk)
    return render(request,'members/Post/detailpost.html',{'post':post})
def UserAccount(request):
    if request.method == "POST":
        form=AccountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountForm()

    return render(request,'members/forms/accountform.html',{'form':form})
