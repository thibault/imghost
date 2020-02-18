from django.urls import path

from images import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('<slug:unique_key>/', views.detail, name='detail'),
]
