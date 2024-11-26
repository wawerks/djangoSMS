from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ScoreForm

@login_required
def score_view(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()  # This will trigger the save method in the model
            return redirect('success_view')  # Redirect to a separate success view
    else:
        form = ScoreForm()
    return render(request, 'score_form.html', {'form': form})
def success_view(request):
    return render(request, 'success.html')
