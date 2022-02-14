from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.utils import timezone
from django.conf import settings
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user) \
            .values_list('to_user_id', flat=True)
        return settings.AUTH_USER_MODEL.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user) \
            .values_list('from_user_id', flat=True)
        return settings.AUTH_USER_MODEL.objects.filter(id__in=user_ids)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'


class Relationship(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user', ]),
        ]


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=200, unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_provincia)


class Canton(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_canton = models.CharField(max_length=200, unique=True)
    rel_prov_canton = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE, db_column='id_user')

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.nombre_canton, self.rel_prov_canton)

    class Meta:
        ordering = ["nombre_canton"]
        verbose_name = "Canton"
        verbose_name_plural = "Cantones"


class Proyectos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    relacion_provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.RESTRICT,
                                           verbose_name='Provincia')
    relacion_canton = models.ForeignKey(Canton, null=False, blank=False, on_delete=models.RESTRICT,
                                        verbose_name='Cantón')
    fecha_creacion = models.DateTimeField()
    monto_ref = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Monto Referencial')
    numero_viviendas = models.IntegerField(verbose_name='Número de viviendas')

    estados_p = [
        ('01', 'Análisis'),
        ('02', 'Ejecución'),
        ('03', 'Finalizado')
    ]
    estado_p = models.CharField(max_length=2, choices=estados_p, default='01', help_text="Escoja un estado")
    observaciones = models.CharField(max_length=200, blank=True
                                     )

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"


class Usuario(AbstractUser):
    areas = [  # para filtrar
        ('01', 'Constructor'),
        ('02', 'Fiscalizador'),
        ('03', 'Administrador de contrato')
    ]
    area_aplica = models.CharField(max_length=2, choices=areas, default='02', help_text="Escoja el área")
    personas = [  # para filtrar
        ('01', 'Natural'),
        ('02', 'Jurídica')
    ]
    tipo = [  # para establecer permisos de usuario

        ('01', 'Oferente'),
        ('02', 'Técnico'),
        ('03', 'Administrador')
    ]
    tipo_persona = models.CharField(max_length=2, choices=personas, default='01')
    cedula = models.CharField(max_length=10, verbose_name='Cedula', unique=True)
    ruc = models.CharField(max_length=13, verbose_name='RUC', unique=True)
    experiencia = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tipo_usuario = models.CharField(max_length=2, choices=tipo, default='01')
    tel_cel = models.CharField(max_length=10, verbose_name='Telf. Celular')
    tel_con = models.CharField(max_length=7, verbose_name='Telf. Convencional')
    direccion = models.CharField(max_length=250, verbose_name='Dirección', blank=True)

    def get_names(self):
        names = self.get_full_name()
        if len(names):
            return names
        return 'Sin nombre'

    def toJSON(self):
        item = model_to_dict(self, exclude=['last_login'])
        item['full_name'] = self.get_full_name()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item[
            'value'] = f'{self.get_full_name()} Tipo: ({self.get_tipo_usuario_display()}) Area: ({self.get_area_aplica_display()})'

        item['experiencia'] = format(self.experiencia, '.2f')
        return item


class Proceso(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    # resolucion = models.CharField(max_length=100)
    objeto = models.CharField(max_length=300)
    tipos = {
        ('01', 'Constructor'),
        ('02', 'Fiscalizador'),
        ('03', 'Administrador de contrato'),
    }
    tipo_contratacion = models.CharField(max_length=2, choices=tipos, default='01')
    forma_pago = models.CharField(max_length=100)
    plazo_entrega = models.IntegerField(verbose_name='Plazo de entrega (meses)')
    Fecha_publica = models.DateField(verbose_name='Fecha de publicación')
    estados = {
        ('01', 'En Trámite'),
        ('02', 'Adjudicado'),
        ('03', 'Fallido')
    }
    estado = models.CharField(max_length=2, choices=estados, default='01')
    Fecha_propuesta = models.DateTimeField(verbose_name='Fecha de entrega de las propuestas')
    Fecha_adjudica = models.DateTimeField(verbose_name='Fecha estimada de adjudicación')
    relacion_proyectos = models.ForeignKey(Proyectos, null=True, verbose_name='Proyecto', blank=True,
                                           on_delete=models.RESTRICT)
    relacion_usuario = models.ForeignKey(Usuario, null=True, verbose_name='Encargado', blank=True,
                                         on_delete=models.RESTRICT)
    monto_experiencia = models.DecimalField(max_digits=20, decimal_places=2)

    personas_p = [
        ('01', 'Natural'),
        ('02', 'Jurídica')
    ]
    dirigido = models.CharField(max_length=2, choices=personas_p, default='01', verbose_name='Dirigido a')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.codigo)



class Invitaciones(models.Model):
    id = models.AutoField(primary_key=True,
                          verbose_name='ID Invitación')
    fecha_crea_invita = models.DateTimeField(auto_now_add=True)
    relacion_usuarioi = models.ForeignKey(Usuario, null=True, verbose_name='Encargado', blank=False,  # este
                                          on_delete=models.RESTRICT, related_name='invita')
    relacion_procesoi = models.ForeignKey(Proceso, null=True, verbose_name='Proceso', blank=False,
                                          on_delete=models.RESTRICT, unique=True)
    fecha_invitacion = models.DateField(null=True, blank=True, default=datetime.now, verbose_name='Fecha')

    def user_email(self):
        return self.relacion_usuarioi.email

    def fecha_propuesta(self):
        return self.relacion_procesoi.Fecha_propuesta

    def __str__(self):
        txt = "{0} {1} {2} {3} {4} {5} {6} {7}"
        return txt.format('ID:', self.id, ' / Proceso: ', self.relacion_procesoi, '/ Encargado:',
                          self.relacion_usuarioi, '/ Correo: ', self.relacion_usuarioi.email)

    class Meta:
        ordering = ["id"]
        verbose_name = "Invitación"
        verbose_name_plural = "Invitaciones"  #


class Invitados(models.Model):
    invitaciones = models.ForeignKey(Invitaciones, db_column='invitaciones_id', on_delete=models.CASCADE,
                                     related_name='rela_invitaciones')
    invitado = models.ForeignKey(Usuario, db_column='id_user', on_delete=models.RESTRICT)
    fecha = models.DateTimeField(null=True, blank=True)
    estados1 = {
        ('01', 'Adjudicado'),
        ('02', 'Invitado')
    }
    estado_invitado = models.CharField(max_length=2, choices=estados1, default='02')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.invitado)

    class Meta:
        ordering = ["invitado"]
        verbose_name = "Invitado"
        verbose_name_plural = "Invitados"


class Adjudica(models.Model):
    invitacion_ad = models.ForeignKey(Invitaciones, on_delete=models.CASCADE, null=True, verbose_name='Invitación')
    fecha_adjudica = models.DateTimeField(null=True)
    adjudicado = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name='Adjudicado')
    fecha_crea = models.DateTimeField(auto_now=True)
    invitados = models.ForeignKey(Invitados, on_delete=models.CASCADE, null=True, verbose_name='Ganador')

    def __str__(self):
        txt = "{0} {1} {2} {3} {4}"
        return txt.format(self.invitacion_ad, ' / Fecha: ', self.fecha_adjudica, ' / Invitado: ', self.invitados)

    class Meta:
        ordering = ["invitacion_ad"]
        verbose_name = "Adjudicación"
        verbose_name_plural = "Adjudicaciones"
