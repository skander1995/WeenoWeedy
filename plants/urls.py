from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from plants import views

urlpatterns = [
    path('', views.PlantList.as_view()),
    path('<int:pk>/', views.PlantDetail.as_view(),name='plant-detail'),
    path('<int:pk>/img/', views.PlantImages.as_view()),
    path('images/', views.PlantImages.as_view(),name='image-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)