from django.shortcuts import render
from demo.forms import ExampleForm

def index(request):
    form = ExampleForm()

    return render(request, 'index.html', {'form': form})

