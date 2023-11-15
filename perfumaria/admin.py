from django.contrib import admin

# Register your models here.
import perfumaria.models as models


admin.site.register(models.Categoria)
admin.site.register(models.Marca)
admin.site.register(models.Perfume)


