from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Taste
from .forms import TasteForm

@login_required
def taste_list(request):
    tastes = Taste.objects.filter(tasted_date__lte=timezone.now()).order_by('tasted_date')
    return render(request, 'rateBeer/taste_list.html', {'tastes': tastes})

@login_required
def taste_detail(request, pk):
    taste = get_object_or_404(Taste, pk=pk)
    return render(request, 'rateBeer/taste_detail.html', {'taste': taste})

@login_required
def taste_new(request):
    if request.method == "POST":
        form = TasteForm(request.POST)
        if form.is_valid():
            taste = form.save(commit=False)
            taste.taster = request.user
            taste.tasting_date = timezone.now()
            taste.save()
            return redirect('taste_detail', pk=taste.pk)
    else:
        form = TasteForm()
        return render(request, 'rateBeer/taste_edit.html', {'form': form})

@login_required
def taste_edit(request, pk):
    taste = get_object_or_404(Taste, pk=pk)
    if request.method == "POST":
        form = TasteForm(request.POST, instance=taste)
        if form.is_valid():
            taste = form.save(commit=False)
            taste.taster = request.user
            taste.tasting_date = timezone.now()
            taste.save()
            return redirect('taste_detail', pk=taste.pk)
    else:
        form = TasteForm(instance=taste)
    return render(request, 'rateBeer/taste_edit.html', {'form': form})

