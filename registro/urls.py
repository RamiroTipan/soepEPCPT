from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
                  path('', views.feed, name='feed'),
                  path('profile/', views.profile, name='profile'),
                  path('profile/<str:username>/', views.profile, name='profile'),
                  path('register/', views.register, name='register'),
                  path('login/', LoginView.as_view(template_name='registro/login.html'), name='login'),
                  path('logout/', LogoutView.as_view(template_name='registro/logout.html'), name='logout'),
                  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
                  path('post/', views.post, name='post'),
                  path('follow/<str:username>/', views.follow, name='follow'),
                  path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
                  path('proyectos', views.proyectos, name='proyectos'),
                  path('invitaciones/', views.InvitacionesListView.as_view(), name='invitaciones'),
                  path('invitaciones_list/', views.InvitacionesTotalListView.as_view(), name='invitaciones_list'),
                  path('user_list/', views.OferentesTotalListView.as_view(), name='user_list'),
                  path('procesos_list/', views.ProcesosTotalListView.as_view(), name='procesos_list'),
                  path('proyectos_list/', views.ProyectosTotalListView.as_view(), name='proyectos_list'),
                  path('adjudicar/', views.AdjudicarInvitaciones.as_view(), name='adjudicar'),
                  path('invitaciones_tot/', views.CrearInvitacionesView.as_view(), name='invitaciones_tot'),
                  path('consultar_user/', views.ConsultarOferentesCal.as_view(), name='consultar_user'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
