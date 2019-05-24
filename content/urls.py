from django.urls import include, path
from . import views

app_name = 'content'

urlpatterns = [

    path('download/', views.download, name='download'),
]
