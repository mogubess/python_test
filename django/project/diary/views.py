from django.contrib.auth.mixins import LoginRequiredMixin # ログイン必須のViewとなる
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day



class IndexView(generic.ListView):
    model = Day
    #デフォルトはday_list.htmlを使う　別ファイルを指定したい場合は
    #template_name _ 'diary/my_list.html'とする
    paginate_by = 3

# Create your views here.
# def index(request):
#     #DBに保存されているDayオブジェクトをすべて取り出す
#     context = {
#         'day_list':Day.objects.all(),
#     }
#     return render(request, 'diary/day_list.html', context)

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    #fields = '__all__'で書き換えることができる
    form_class = DayCreateForm
    #success_urlデータの追加に成功した場合のリダイレクト先
    #reverse_lazyはURLの文字列を返す
    success_url = reverse_lazy('diary:index') 


# def add(request):
#     # context = {
#     #     'form':DayCreateForm()
#     # }
#     # return render(request,'diary/day_form.html',context)
#     form = DayCreateForm(request.POST or None)

#     #form.is_valid()で入力内容に問題がないかをCheck　日付であればそのフォーマットもCheckする
#     if request.method == 'POST' and form.is_valid():
#         form.save() #DBにまで保存される
#         return redirect('diary:index') #任意のURLへ誘導する

#     context = {
#         'form':form
#     }
#     return render(request, 'diary/day_form.html',context)

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


# def update(request, pk):
#     day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

#     form = DayCreateForm(request.POST or None, instance=day)

#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('diary:index')
    
#     context = {
#         'form':form
#     }
#     return render(request,'diary/day_form.html', context)

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')


# def delete(request, pk):
#     day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

#     if request.method == 'POST':
#         day.delete()
#         return redirect('diary:index')
    
#     context = {
#         'day':day
#     }
#     return render(request,'diary/day_confirm_delete.html', context)

class DetailView(generic.DetailView):
    model = Day



# def detail(request, pk):
#     day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

#     context = {
#         'day':day
#     }
#     return render(request,'diary/day_detail.html', context)

