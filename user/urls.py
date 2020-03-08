from django.urls import path
from . import views
urlpatterns = [

    path('',views.register,name="register"),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
]