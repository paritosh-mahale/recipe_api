from django.urls import path
from .views import RecipeView, RecipeDetails
from rest_framework.authtoken import views

urlpatterns = [
    path('', RecipeView.as_view()),
    path('<int:pk>', RecipeDetails.as_view()),
]