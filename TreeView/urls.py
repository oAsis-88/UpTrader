from django.urls import path

from TreeView.views import show_menu

app_name = "TreeView"

urlpatterns = [
    path('<str:name>/', show_menu, name='show_menu'),
    path('', show_menu),
]