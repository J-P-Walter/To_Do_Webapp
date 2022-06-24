from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
import datetime

# Create your views here.
def home_view(request):
    all_tasks = ToDoList.objects.all()
    today_date = datetime.datetime.now().date()
    prev_date = datetime.datetime.now().date() - datetime.timedelta(days=1)

    prev_tasks = []
    today_task = []
    week_tasks = []
    future_tasks = []

    for task in all_tasks:
        if (task.date < prev_date):
            task.delete()
        if (task.date == prev_date and task.done == False):
            prev_tasks.append(task)
        elif (task.date == prev_date and task.done == True): #Maybe not delete??
            task.delete()
        elif (task.date == today_date):
            today_task.append(task)
        elif (task.date.strftime("%V") == datetime.date.today().strftime("%V")):
            week_tasks.append(task)
        else:
            future_tasks.append(task)
    context = {
        "prev_tasks": prev_tasks, 
        "today_tasks": today_task, 
        "week_tasks": week_tasks,
        "future_tasks": future_tasks
    }
    return render(request, "home.html", context)

def create_view(request):
    form = ToDoListForm(request.POST or None)
    if (form.is_valid()):
        form.save()

        return redirect('http://127.0.0.1:8000/')
    context = {
        'form': form
    }
    return render(request, "todo_create.html", context)

def edit_view(request, id):
    obj = ToDoList.objects.get(id=id)
    
    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance = obj)
        if (form.is_valid()):
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = ToDoListForm(instance = obj)

    context = {
        'form': form
    }
    return render(request, "todo_edit.html", context)

def delete_view(request, id):
    obj = ToDoList.objects.get(id=id)
    obj.delete()
    return redirect('http://127.0.0.1:8000/')

def mark_view(request, id):
    obj = ToDoList.objects.get(id=id)
    obj.done = not obj.done
    obj.save()
    return redirect('http://127.0.0.1:8000/')