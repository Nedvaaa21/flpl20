from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Soft
from .forms import SoftForm
from django.core.paginator import Paginator
from django.views.generic import ListView


class IndexTab(ListView):
    paginate_by = 5
    model = Soft
    template_name = 'main/index_tab.html'
    context_object_name = 'softs'
    extra_context = {
        'numbers': 'із' + str(len(Soft.objects.all()))
    }
    allow_empty = False

def index(request):
    softs = Soft.objects.all()
    # softs = Soft.objects.sort_by('-id')
    return render(request, 'main/index.html', {
        'title': 'Головна сторінка',
        'softs': softs
    })

def index_tab(request):
    softs = Soft.objects.all()
    # softs = Soft.objects.sort_by('-id')
    return render(request, 'main/index_tab.html', {
        'title': 'Головна сторінка',
        'softs': softs
    })

def soft_view(request, id = 1):
    try:
        softs = Soft.objects.get(id=id)
    except Soft.DoesNotExists:
        raise Http404
    return render(request, 'main/soft_view.html', {
        'title': 'Обрана книга',
        'softs': softs
    })


def soft_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = SoftForm()
        else:
            soft = Soft.objects.get(id=id)
            form = SoftForm(instance=soft)
        return render(request,
                      'main/soft_edit.html',
                      {'form': form})
    else:
        if id == 0:
            form = SoftForm(request.POST)
        else:
            soft = Soft.objects.get(id=id)
            form = SoftForm(request.POST, instance=soft)
        if form.is_valid():
            form.save()
        return redirect('main')

def soft_delete(request, id=0):
    try:
        softs = Soft.objects.get(id=id)
        softs.delete()
    except Soft.DoesNotExists:
        raise Http404
    soft = Soft.objects.order_by('-id')
    return render(request, 'main/index_tab.html',
                    {
                      'title': 'Книги',
                      'soft': soft
                  })




def about(request):

    context_list = Soft.objects.all()
    paginator = Paginator(context_list, 5)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'main/about.html', {
        'title': 'About US',
        'softs_page': page_obj
    })

def index_start(request):
    return render(request, 'main/start.html')


def create(request):
    if request.method == 'POST':
        form = SoftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')




    form = SoftForm(initial={
        'title': 'Невідома назва',
        'author': 'Невідомий автор',
        'text': 'Опис відсутній',
        'published': '2023',
        'count': 1
    })
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)