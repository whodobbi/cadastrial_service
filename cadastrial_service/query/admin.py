from django.contrib import admin
from query.models import CadastrialQuery


class CadastrialQueryAdmin(admin.ModelAdmin):
    list_display = (
        "cadastrial_number",
        "latitude",
        "longitude",
        "result",
        "timestamp",
    )
    search_fields = ("cadastrial_number",)

admin.site.register(CadastrialQuery, CadastrialQueryAdmin)
