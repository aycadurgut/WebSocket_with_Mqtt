from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CustomUserCreate, MyObtainTokenPairView


urlpatterns = [
#     path('login', views.login_request, name="login"),
#     path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('register', RegisterView.as_view(), name="register"),
#     path('logout', views.logout_request, name="logout"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('token/', MyObtainTokenPairView.as_view(), name='token'),
]



