from django.shortcuts import render, redirect
from .models import Personal
from index.forms import PersonalForm, EditarPersonalForm
from django.contrib import messages

# Create your views here.
def inicio_view(request):
    return render(request, 'inicio.html')

def personal_view(request):

    form_personal = PersonalForm()
    form_editar_personal = EditarPersonalForm()
    personal = Personal.objects.all()

    context = {
        'form_personal': form_personal,
        'personal': personal,
        'form_editar_personal': form_editar_personal,

    }
    return render(request, 'personal.html', context)

def add_personal_view(request):
    if request.POST:
        #print(request.POST)
        form = PersonalForm(request.POST, request.FILES)
        if form.is_valid():
            print("Si llegamos hasta aqui")
            try:
                form.save()
            except:
                messages.warning(request,"Personal ya agregado o datos incorrectos")
                return redirect('personal')


    return redirect('personal')

def edit_personal_view(request):
    if request.POST:
        producto = Personal.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarPersonalForm(
            request.POST, request.FILES, instance=producto)
        if form.is_valid:
            form.save()

    return redirect('personal')

def delete_personal_view(request):
    if request.POST:
        personal = Personal.objects.get(pk=request.POST.get('id_personal_eliminar'))
        personal.delete()
    return redirect('personal')
