from django.shortcuts import render

def pet_list(request):
    return render(request, "pets/pet_list.html")