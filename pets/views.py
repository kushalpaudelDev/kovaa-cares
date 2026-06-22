from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

# LIST
@login_required
def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "pets/pet_list.html", {"pets": pets})

# CREATE
@login_required
def pet_create(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.owner = request.user
        pet.save()
        return redirect('pet_list')
    return render(request, "pets/pet_form.html", {"form": form})

# UPDATE
@login_required
def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if pet.owner != request.user:
        return redirect('pet_list')
    form = PetForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('pet_list')
    return render(request, "pets/pet_form.html", {"form": form})

# DELETE
@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if pet.owner != request.user:
        return redirect('pet_list')
    if request.method == "POST":
        pet.delete()
        return redirect('pet_list')
    return render(request, "pets/pet_delete.html", {"pet": pet})