from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm

# LIST
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, "pets/pet_list.html", {"pets": pets})

# CREATE
def pet_create(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pet_list')
    return render(request, "pets/pet_form.html", {"form": form})

# UPDATE
def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    form = PetForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('pet_list')
    return render(request, "pets/pet_form.html", {"form": form})

# DELETE
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('pet_list')
    return render(request, "pets/pet_delete.html", {"pet": pet})