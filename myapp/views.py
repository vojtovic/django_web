from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Body_part ,Equipment, Difficulty ,Exercise


def index(request):
    body_part = 'exercises'
    context = {
        'nadpis': body_part,
        'exercises': Exercise.objects.order_by('name'),
        'body_parts': Body_part.objects.order_by('body_part'),
        'difficulties': Difficulty.objects.all(),
        'equipments': Equipment.objects.all()
    }
    return render(request, 'index.html', context=context)

class ExerciseDetail(DetailView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'detail.html'
    context = {
        'exercises': Exercise.objects.order_by('name'),
        'body_parts': Body_part.objects.order_by('body_part'),
        'difficulties': Difficulty.objects.all(),
        'equipments': Equipment.objects.all()
    }
class ExerciseView(ListView):
    model = Exercise
    context_object_name = 'exercises'
    template_name = 'list.html'

