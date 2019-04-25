from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Feature
from django.contrib.auth.decorators import login_required
from .forms import FeatureForm

# Create your views here.
def all_features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})
    
login_required()
def add_feature(request, pk=None):
    feature =  get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)
        
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            return redirect('feature_details', feature.pk)
            
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'add_feature.html', {'form':form})
    
@login_required() 
def feature_details(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            featureDescrip = form.save(commit=False)
            featureDescrip.feature = feature
            featureDescrip.author = request.user
            featureDescrip.save()
            return redirect(reverse('feature_details', kwargs={'pk': pk}))
             
    else:
        form = FeatureForm()
        feature.views += 1
        feature.save()
    return render(request, 'feature_details.html', {'feature':feature, 'form':form})    