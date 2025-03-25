
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento, Logistica, MaterialMarketing, Demanda, Usuario, Material
from .forms import EventoForm, RecursoForm, DemandaForm, MaterialMarketingForm
from django.core.paginator import Paginator

# Sistema de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

# Página Inicial
def home(request):
    return render(request, 'home.html')

# Agenda

def listar_eventos(request):
    # Ordena por data_horario de forma ascendente (mais antiga para mais nova)
    eventos = Evento.objects.all().order_by('data_horario')
    paginator = Paginator(eventos, 10)  # Exibe 10 eventos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'evento/listar_eventos.html', {'page_obj': page_obj})

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('listar_eventos')
        else:
            messages.error(request, 'Houve um erro ao criar o evento.')
    else:
        form = EventoForm()
    return render(request, 'evento/criar_evento.html', {'form': form})

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'evento/editar_evento.html', {'form': form, 'evento': evento})

@login_required
def deletar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, criado_por=request.user)
    evento.delete()
    return redirect('listar_eventos')

# Logística
def listar_recursos(request):
    recursos = Logistica.objects.all()
    return render(request, 'logistica/recursos.html', {'recursos': recursos})

def criar_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_recursos')
    else:
        form = RecursoForm()
    return render(request, 'logistica/criar_recurso.html', {'form': form})

def planejamento_rotas(request):
    return render(request, 'logistica/planejamento_rotas.html')

# Marketing
def listar_materiais(request):
    materiais = MaterialMarketing.objects.all()
    return render(request, 'materiais/listar_materiais.html', {'materiais': materiais})

def aprovar_material(request, material_id):
    material = get_object_or_404(MaterialMarketing, id=material_id)
    material.aprovado = True
    material.save()
    return redirect('listar_materiais')

# Demandas
def listar_demandas(request):
    demandas = Demanda.objects.all()
    return render(request, 'demandas/listar_demandas.html', {'demandas': demandas})

def criar_demanda(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_demandas')
    else:
        form = DemandaForm()
    return render(request, 'demandas/criar_demanda.html', {'form': form})

def detalhe_demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)
    return render(request, 'demandas/detalhe_demanda.html', {'demanda': demanda})


# def criar_material(request):
#     if request.method == 'POST':
#         form = MaterialMarketingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_materiais')  # Redireciona para a lista de materiais
#     else:
#         form = MaterialMarketingForm()
#     return render(request, 'marketing/criar_material.html', {'form': form})

def criar_material(request):
    if request.method == 'POST':
        form = MaterialMarketingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_materiais')  # Redireciona para a lista de materiais
    else:
        form = MaterialMarketingForm()
    return render(request, 'materiais/criar_material.html', {'form': form})


def editar_material(request, material_id):
    material = get_object_or_404(MaterialMarketing, id=material_id)
    if request.method == 'POST':
        form = MaterialMarketingForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('listar_materiais')
    else:
        form = MaterialMarketingForm(instance=material)
    return render(request, 'materiais/editar_material.html', {'form': form, 'material': material})


def aprovar_material(request, material_id):
    material = get_object_or_404(MaterialMarketing, id=material_id)
    material.aprovado = True
    material.save()
    return redirect('listar_materiais')


def deletar_material(request, material_id):
    material = get_object_or_404(MaterialMarketing, id=material_id)
    material.delete()
    return redirect('listar_materiais')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')  # Renderiza o template do Dashboard

# View para listar coordenadores
def listar_coordenadores(request):
    coordenadores = Usuario.objects.filter(tipo='coordenador')  # Filtra apenas os coordenadores
    return render(request, 'coordenadores/listar_coordenadores.html', {'coordenadores': coordenadores})

# View para listar lideranças
def listar_liderancas(request):
    liderancas = Usuario.objects.filter(tipo='lideranca')  # Filtra apenas as lideranças
    return render(request, 'liderancas/listar_liderancas.html', {'liderancas': liderancas})

# View para listar eleitores
def listar_eleitores(request):
    eleitores = Usuario.objects.filter(tipo='eleitor')  # Filtra apenas os eleitores
    return render(request, 'eleitores/listar_eleitores.html', {'eleitores': eleitores})




def listar_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'materiais/listar_materiais.html', {'materiais': materiais})
