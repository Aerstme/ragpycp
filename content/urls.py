from django.urls import include, path
from . import views

app_name = 'content'

# ADD URLs FOR CUSTOM PAGES HERE

urlpatterns = [

    path('download/', views.download, name='download'),
]
