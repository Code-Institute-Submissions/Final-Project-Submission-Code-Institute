from django.shortcuts import render

# Create your views here.
def index(request):
    """A view to display the index page"""
    return render(request, "index.html")