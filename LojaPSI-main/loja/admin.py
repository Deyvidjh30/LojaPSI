from django.contrib import admin
from .models import * #imporata nossos models

class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('produtoo', 'destaque', 'promocao', 'msgPromocao',
    'preco', 'categoria',)
    empty_value_display = 'Vazio'

#admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)

# Register your models here.
