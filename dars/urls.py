from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestApiViews.as_view()),
    path("test/<int:pk>", views.TestDetailApiViews.as_view())
]
