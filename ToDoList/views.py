from django.shortcuts import render
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
        elif (task.date == prev_date and task.done == True):
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
        form = ToDoListForm()
    context = {
        'form': form
    }
    return render(request, "todo_create.html", context)