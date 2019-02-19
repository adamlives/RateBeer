from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Taste

def taste_list(request):
    tastes = Taste.objects.filter(tasted_date__lte=timezone.now()).order_by('tasted_date')
    return render(request, 'rateBeer/taste_list.html', {'tastes': tastes})

def taste_detail(request, pk):
    taste = get_object_or_404(Taste, pk=pk)
    return render(request, 'rateBeer/taste_detail.html', {'taste': taste})