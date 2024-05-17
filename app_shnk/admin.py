from django.contrib import admin

from .models import (
    SHNKSystemsModel,
    SHNKGroupsModel,
    SHNKTypesModel,
    SHNKDocumentsModel,
    SHNKDocPartsModel,
    SHNKDocPlansModel,
)

# Register your models here.
admin.site.register(SHNKSystemsModel)
admin.site.register(SHNKGroupsModel)
admin.site.register(SHNKTypesModel)
admin.site.register(SHNKDocumentsModel)
admin.site.register(SHNKDocPartsModel)
admin.site.register(SHNKDocPlansModel)
