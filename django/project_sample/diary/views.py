from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

# Create your views here.
def index(request):
    #DBに保存されているDayオブジェクトをすべて取り出す
    context = {
        'day_list':Day.objects.all(),
    }
    return render(request, 'diary/day_list.html', context)


def add(request):
    # context = {
    #     'form':DayCreateForm()
    # }
    # return render(request,'diary/day_form.html',context)
    form = DayCreateForm(request.POST or None)

    #form.is_valid()で入力内容に問題がないかをCheck　日付であればそのフォーマットもCheckする
    if request.method == 'POST' and form.is_valid():
        form.save() #DBにまで保存される
        return redirect('diary:index') #任意のURLへ誘導する

    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html',context)

def update(request, pk):
    day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    

    context = {
        'form':form
    }
    return render(request,'diary/day_form.html', context)

def delete(request, pk):
    day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')
    
    context = {
        'day':day
    }
    return render(request,'diary/day_confirm_delete.html', context)

def detail(request, pk):
    day = get_object_or_404(Day,pk=pk) #DB内に当該数字のデータがあるかＣｈｅｃｋなければ４０４を返す

    context = {
        'day':day
    }
    return render(request,'diary/day_detail.html', context)
