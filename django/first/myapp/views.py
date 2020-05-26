#from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse("Hello, world",charset='cp932')
#    return render(request, 'myapp/index.html')
    context = {'name':'Boku'}
    return render(request, 'myapp/index.html', context)

def about(request):
    """/aboutページ"""
    return render(request, 'myapp/about.html')

def info(request):
    """/infoページ"""
    return render(request, 'myapp/info.html')


#renderを使わない場合の表示方法
# from django.http import HttpResponse
# from django.template import loader

# def index(request):
#     template = loader.get
#     context = {
#         'name':'Boku'
#     }
#     reponse_src = template.render(context,request)
#     return HttpResponse(response_src)
