from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms import EtudiantForm

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste_etudiants.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form})

def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer_etudiant.html', {'etudiant': etudiant})