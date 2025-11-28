from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/',views.Register.as_view(), name='register' ),
    path('contact/',views.ContactView.as_view(), name='contact' ),
    path("firebase-config/", views.FirebaseConfig.as_view(), name="firebase-config"),
    path("firebase-login/", views.FirebaseLogin.as_view(), name="firebase-login"),
]