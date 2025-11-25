from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register',views.Register.as_view(), name='register' ),
]