from django.shortcuts import render
from .forms import CategoryForm

# Create your views here.


def create_category(request):
    form = CategoryForm()
    return render(request, 'trip/pages/create_category.html', {'form': form})
