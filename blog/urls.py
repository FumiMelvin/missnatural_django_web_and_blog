from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.bloghome, name='bloghome'),
    path('<slug:slug>/', views.getpost, name='post')
]
 