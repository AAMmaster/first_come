
from django.urls import path
from .views import (
    RecipeListView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('create/', RecipeCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', RecipeUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete'),
]