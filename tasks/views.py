from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    category = request.GET.get('category')
    priority = request.GET.get('priority')

    tasks = Task.objects.filter(user=request.user)

    if category:
        tasks = tasks.filter(category=category)
    if priority:
        tasks = tasks.filter(priority=priority)

    paginator = Paginator(tasks, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='CO').count()

    completion_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    return render(request, 'tasks/task_list.html', {
        'page_obj': page_obj,
        'completion_percentage': completion_percentage,
        'category': category,
        'priority': priority,
    })

@login_required
def task_create(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'tasks/task_form.html', {'form': form})

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        else:
            return render(request, 'tasks/task_form.html', {'form': form})

def get_queryset(self):
    queryset = super().get_queryset()

    if self.request.user.is_authenticated:
        queryset = queryset.filter(assigned_to=self.request.user)
        return queryset

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})