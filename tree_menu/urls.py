from django.urls import path
from tree_menu import views as views_tree_menu

app_name = 'tree_menu'

urlpatterns = [

    path('menu/', views_tree_menu.IndexView.as_view()),

]