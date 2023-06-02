from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    fields = '__all__'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')