from django.contrib import admin
from .models import Post, Profile, Relationship, Provincia, Canton, Proyectos, Usuario, Proceso, Invitaciones, Invitados, Adjudica
# from import_export.admin import ImportExportModelAdmin - crear importar y exportar
admin.site.site_header = 'Administración del sistema de selección de oferentes'
admin.site.index_title ='EPCPT'
admin.site.site_title = 'Registro de oferentes'
admin.site.register(Profile)
# admin.site.register(Relationship)
# admin.site.register(Provincia)
# admin.site.register(Canton)
# admin.site.register(Proyectos)
# admin.site.register(Usuario)
admin.site.register(Proceso)
# admin.site.register(Invitados)

admin.site.register(Adjudica)
#admin.site.register(Post)


# admin.site.register(Invitaciones)


class Detalle_InvitacionesInLine(admin.TabularInline):
    model = Invitados


class Invitaciones_Admin(admin.ModelAdmin):
    inlines = (Detalle_InvitacionesInLine,)
    list_filter = ('relacion_usuarioi', 'relacion_procesoi')
    list_display = ('id', 'relacion_procesoi', 'relacion_usuarioi', 'user_email', 'fecha_propuesta')
    # search_fields = ('Detalle_invitacionesInLine.invitado',)---> no funciono


class Detalle_CantonesInLine(admin.TabularInline):
    model = Canton



class Provincias_Admin(admin.ModelAdmin):
    inlines = (Detalle_CantonesInLine,)
    search_fields = ('nombre_provincia',)
    ordering = ('nombre_provincia',)
    list_per_page = 10


class Detalle_ProcesosInLie(admin.TabularInline):
    model = Proceso
    list_display = ('nombre', 'relacion_provincia', 'estado')


class Procesos_admin(admin.ModelAdmin):
    inlines = (Detalle_ProcesosInLie,)
    search_fields = ('nombre',)
    list_display = ('nombre', 'relacion_provincia', 'relacion_canton')
    list_filter = ('relacion_provincia',)


class Usuario_admin(admin.ModelAdmin):
    list_display = ('username', 'tipo_persona', 'first_name', 'last_name', 'tel_cel', 'experiencia', 'area_aplica', 'date_joined')
    list_filter = ('tipo_persona', 'area_aplica', 'date_joined')
    list_per_page = 10
   # list_select_related =


class Invitados_admin(admin.ModelAdmin):
    search_fields = ('invitado__username', 'invitaciones__id')
    list_display = ('invitaciones', 'invitado', 'estado_invitado')
    list_filter = ('estado_invitado', 'invitaciones__relacion_procesoi')
    list_editable = ('estado_invitado', )
    list_per_page = 10


admin.site.register(Provincia, Provincias_Admin)
admin.site.register(Invitaciones, Invitaciones_Admin)
admin.site.register(Proyectos, Procesos_admin)
admin.site.register(Usuario, Usuario_admin)
admin.site.register(Invitados, Invitados_admin)

# Crea importar y exportar
# @admin.register(Invitaciones)
# class InvitacionesAdmin(ImportExportModelAdmin):
#     pass
