from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
#from .froms import TodoCreateFrom
from . import forms
# Create your views here.


def Home(request):
	all = Todo.objects.all()
	return render(request,'home.html',{'todos':all})


def detail(request, todo_id):
	todo = Todo.objects.get(id=todo_id)
	return render(request,'detail.html', {'todo':todo})


def delete(request, todo_id):
	Todo.objects.get(id=todo_id).delete()
	messages.success(request, "you delete seccessfully!", extra_tags='success')
	return redirect('home')

def create(request):
	if request.method == 'POST':
		form = forms.TodoCreateFrom(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			Todo.objects.create(title=cd['title'],body=['body'],time=['time'])
			messages.success(request, "Add seccessfully!",'success')
			return redirect('home')
	else:
		form = forms.TodoCreateFrom()
	return render(request, 'create.html',{'forms':forms})