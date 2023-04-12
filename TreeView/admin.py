from django.contrib import admin

from TreeView.models import Paragraph


class AdminParagraph(admin.ModelAdmin):
    list_display = ('title', 'parent')


admin.site.register(Paragraph, AdminParagraph)
