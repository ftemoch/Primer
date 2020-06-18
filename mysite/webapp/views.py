from django.shortcuts import render, redirect
from django.http import HttpResponse
#importa el modulo inlinefromset
from django.forms import  inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
#Para restringir el uso de las paginas
from django.contrib.auth.decorators import login_required
#Para adicionar al momento de registro de un nuevo usuario group=cliente
from django.contrib.auth.models import Group


# Create your views here.
from .models import *
from .forms import ContratoForm
from .forms import Contrato1Form, CreateUserForm
from .filters import ContratoFilter
from .decorators import usuario_noautenticado, usuario_permitido, solo_admin

@usuario_noautenticado
def registerPage(request):
    #if request.user.is_authenticated:
    #    return redirect('inicio')
    #else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                usuario = form.save()
                nombre_usuario = form.cleaned_data.get('username')
                grupo = Group.objects.get(name='cliente')
                usuario.groups.add(grupo)
                messages.success(request, 'Registro usuario ok..' + nombre_usuario)
                return redirect('login')

        context = {'form': form}
        return render(request, 'webapp/register.html', context)

@usuario_noautenticado
def loginPage(request):
    #if request.user.is_authenticated:
    #    return redirect('inicio')
    #else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.info(request, 'usuario o contraseña incorrecta..')

        context = {}
        return render(request, 'webapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# Con esto restringimos la pagina solo para usuarios logueados
@login_required(login_url='login')
#@solo_admin
@usuario_permitido(allowed_roles=['admin', 'cliente'])
def home(request):
    contratos = Contrato.objects.all().order_by('cliente')
    clientes = Cliente.objects.all()
    total_clientes = clientes.count()
    total_contratos = contratos.count()
    ejecucion = contratos.filter(estado_contrato="En ejecucion").count()
    pendiente = contratos.filter(estado_contrato="Pendiente").count()
    context = {'contratos': contratos, 'clientes': clientes,
               'total_clientes': total_clientes, 'total_contratos': total_contratos,
               'ejecucion': ejecucion, 'pendiente': pendiente}

    return render(request, 'webapp/dashboard.html', context)

def userPage(request):
    context = {}
    return render(request, 'webapp/user.html', context)

@login_required(login_url='login')

@usuario_permitido(allowed_roles=['admin'])
def productos(request):
    equipos = Equipo.objects.all()
    return render(request, 'webapp/productos.html', {'equipos': equipos})

@login_required(login_url='login')
@usuario_permitido(allowed_roles=['admin'])
def clientes(request, pk_test):
    cliente = Cliente.objects.get(id=pk_test)

    contratos = cliente.contrato_set.all()
    contrato_count = contratos.count()

    myFilter = ContratoFilter(request.GET, queryset=contratos)

    contratos = myFilter.qs

    context = {'cliente': cliente, 'contratos': contratos, 'contrato_count': contrato_count,
               'myFilter':myFilter}
    return render(request, 'webapp/clientes.html', context)

@login_required(login_url='login')
@usuario_permitido(allowed_roles=['admin'])
def crearContrato1(request):

    form = Contrato1Form()


    #Que pasa si le damos submit al formulario
    if request.method == 'POST':
        print('Imprimiendo el formulario: ', request.POST)
        form = Contrato1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'webapp/contrato1_form.html', context)

@login_required(login_url='login')
@usuario_permitido(allowed_roles=['admin'])
def crearContrato(request, pk):
    ContratoFromSet = inlineformset_factory(Cliente, Contrato, fields=('equipo', 'estado_contrato'), extra=5)
    cliente = Cliente.objects.get(id=pk)
    formset = ContratoFromSet(queryset=Contrato.objects.none(),instance=cliente)
    #form = ContratoForm(initial={'cliente':cliente})
    if request.method == 'POST':
        print('Imprimiendo el formulario: ', request.POST)
        formset = ContratoFromSet(request.POST, instance=cliente)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset, 'cliente':cliente}
    return render(request, 'webapp/contrato_form.html', context)

@login_required(login_url='login')
@usuario_permitido(allowed_roles=['admin'])
def actualizarContrato(request, pk):

    # contrato = Contrato.objects.get(id=pk)
    # form = ContratoForm(instance=contrato)
    # if request.method == 'POST':
    #     form = ContratoForm(request.POST, instance=contrato)
    #     if form.is_valid():
    #         form.save()
    #        return redirect('/')
    contrato = Contrato.objects.get(id=pk)
    form = Contrato1Form(instance=contrato)
    # Que pasa si le damos submit al formulario para actualizar
    if request.method == 'POST':
        print('Actualizando el formulario: ', request.POST)
        form = Contrato1Form(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'webapp/contrato1_form.html', context)

@login_required(login_url='login')
@usuario_permitido(allowed_roles=['admin'])
def borrarContrato(request, pk):
    contrato = Contrato.objects.get(id=pk)
    if request.method == "POST":
        contrato.delete()
        return redirect('/')
    context = {'item': contrato}
    return render(request, 'webapp/borrar.html', context)
