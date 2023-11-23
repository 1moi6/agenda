from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UsuarioRegistroView, AdmTokenPairView

urlpatterns = [
    path('cadastro/', UsuarioRegistroView.as_view(), name='cadastro'),
    path('token/', AdmTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]