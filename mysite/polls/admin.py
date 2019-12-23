from django.contrib import admin

from .models import Empleado
from .models import Departamento
from .models import Especialidad
from .models import Servicio
from .models import Reporte
from .models import ReporteDetalle
from .models import Cliente
from .models import CompraProducto
from .models import Producto
from .models import Contato


admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Especialidad)
admin.site.register(Servicio)
admin.site.register(Reporte)
admin.site.register(ReporteDetalle)
admin.site.register(Cliente)
admin.site.register(CompraProducto)
admin.site.register(Producto)
admin.site.register(Contato)