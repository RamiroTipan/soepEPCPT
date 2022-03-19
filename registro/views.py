import json

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, FormView
from .models import *
from .forms import UserRegisterForm, PostForm, CrearProyectosForm, MostrarInvitacionesForm, CrearAdjudicacionesForm, \
    CrearInvitacionesForm, ChildFormset, InvitacionesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'registro/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registro/register.html', context)


@login_required
def post(request):
    current_user = get_object_or_404(Usuario, pk=request.user.pk)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'registro/post.html', {'form': form})


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = Usuario.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'registro/profile.html', {'user': user, 'posts': posts})


def follow(request, username):
    current_user = request.user
    to_user = Usuario.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('feed')


def unfollow(request, username):
    current_user = request.user
    to_user = settings.AUTH_USER_MODEL.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')


def proyectos(request):
    if request.method == 'POST':
        form = CrearProyectosForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = CrearProyectosForm()

    context = {'form': form}
    return render(request, 'registro/register.html', context)


def invitaciones(request):
    if request.method == 'POST':
        form = MostrarInvitacionesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = MostrarInvitacionesForm()

    context = {'form': form}

    return render(request, 'registro/register.html', context)


class InvitacionesListView(ListView):
    model = Invitaciones
    template_name = 'registro/invitaciones.html'

    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        usuario1 = request.user.get_username()
        procesoA = Proceso.objects.all().select_related('relacion_procesoi').values_list(
            'relacion_proyectos__proceso__Fecha_propuesta')
        oferentes1 = Invitados.objects.filter(invitado__username__contains=usuario1)
        if oferentes1:
            print("ha consultado por oferente")
        else:
            print("ha consultado por proceso")
        return render(request, 'registro/invitaciones.html', {'oferentes1': oferentes1, 'procesoA': procesoA})


class InvitacionesTotalListView(ListView):
    model = Invitaciones
    template_name = 'registro/invitaciones_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OferentesTotalListView(ListView):
    model = Usuario
    template_name = 'registro/user_list.html'
    ordering = ['-date_joined']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProcesosTotalListView(ListView):
    model = Proceso
    template_name = 'registro/procesos_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProyectosTotalListView(ListView):
    model = Proyectos
    template_name = 'registro/proyectos_list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AdjudicarInvitaciones(CreateView):
    model = Adjudica

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        action = request.POST['action']
        if action == 'search_product_id':
            data = []
            for i in Invitaciones.objects.filter(relacion_procesoi__invitaciones=request.POST['id']):
                data.append({'id': i.id, 'name': i.relacion_usuarioi})

    form_class = CrearAdjudicacionesForm
    template_name = 'registro/adjudicar.html'
    success_url = reverse_lazy('adjudicar')


class ConsultarOferentesCal(ListView):
    model = Usuario
    template_name = 'registro/consultar_user.html'


class InvitacionesNested(ListView):
    model = Invitaciones


class CrearInvitacionesView(FormView):

    template_name = 'registro/invitaciones_tot.html'
    form_class = InvitacionesForm
    success_url = reverse_lazy('invitaciones_tot')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            print(request.POST)
            if action == 'search_invitations':
                data = []
                proceso_id = request.POST.get('procesos', '')
                if len(proceso_id):
                    proceso = Proceso.objects.get(pk=proceso_id)
                    users = Usuario.objects.filter(area_aplica=proceso.tipo_contratacion, tipo_persona=proceso.dirigido,
                                                   experiencia__gte=proceso.monto_experiencia)
                    for u in users:
                        data.append({
                            'id': u.id,
                            'nombres': u.get_names(),
                            'cedula': u.cedula,
                            'tipo_persona': u.get_tipo_persona_display(),
                            'experiencia': format(u.experiencia, '.2f'),
                            # 'tipo_usuario': u.get_tipo_usuario_display(),
                            'area_aplica': u.get_area_aplica_display(),

                            'state': 0
                        }
                        )
            elif action == 'create_invitation':
                with transaction.atomic():
                    items = json.loads(request.POST['items'])
                    proceso_id = request.POST['procesos']
                    detail = Invitaciones()
                    detail.relacion_usuarioi_id = request.user.id
                    detail.relacion_procesoi_id = proceso_id
                    detail.save()
                    for i in items:
                        invitado = Invitados()
                        invitado.invitaciones_id = detail.id
                        invitado.invitado_id = i['id']
                        invitado.fecha = datetime.now().date()
                        invitado.save()
            elif action == 'search_users':
                data = []
                proceso_id = request.POST['id']
                if len(proceso_id):
                    proceso = Proceso.objects.get(pk=proceso_id)
                    users = Usuario.objects.filter(area_aplica=proceso.tipo_contratacion, tipo_persona=proceso.dirigido,
                                                   experiencia__gte=proceso.monto_experiencia)
                    for u in users:
                        data.append({'id': u.id, 'full_name': u.get_names()})
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

