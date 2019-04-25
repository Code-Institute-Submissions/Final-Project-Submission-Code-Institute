from django.shortcuts import render, redirect
from .models import Bug
from django.contrib.auth.decorators import login_required
from .forms import BugForm

# Create your views here.
@login_required()
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    

@login_required()  
def add_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST)

        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            bug.author = request.user
            return redirect('bugs')
    else:
        form = BugForm()
    return render(request, 'add_bug.html', {'form':form})