from django.shortcuts import render

from demo.forms import ExampleForm


def index(request):
    form = ExampleForm()

    return render(request, 'index.html', {'form': form})


def basic(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        return render(request, 'basic_done.html')

    return render(request, 'basic.html', {'form': form})


def horizontal(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        return render(request, 'basic_done.html')

    return render(request, 'horizontal.html', {'form': form})
