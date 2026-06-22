from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


@login_required
def review_create(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('review_list')
    return render(request, 'reviews/review_form.html', {'form': form})


@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return redirect('review_list')
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('review_list')
    return render(request, 'reviews/review_form.html', {'form': form})


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return redirect('review_list')
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'reviews/review_delete.html', {'review': review})
