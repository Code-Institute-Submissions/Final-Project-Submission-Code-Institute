from django.shortcuts import render, redirect, get_object_or_404, reverse
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
    

@login_required() 
def bug_details(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bugDescrip = form.save(commit=False)
            bugDescrip.bug = bug
            bugDescrip.author = request.user
            bugDescrip.save()
            return redirect(reverse('bug_details', kwargs={'pk': pk}))
             
    else:
        form = BugForm()
        bug.views += 1
        bug.save()
    return render(request, 'bug_details.html', {'bug':bug, 'form':form})