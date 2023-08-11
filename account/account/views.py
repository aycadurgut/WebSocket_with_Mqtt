# from rest_framework.decorators import api_view, permission_classes
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from account.forms import LoginUserForm, NewUserForm
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from .serializers import UserSerializer
# from rest_framework.views import APIView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from django.contrib.auth.models import User
from .serializers import MyTokenObtainPairSerializer

class CustomUserCreate(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer

class BlacklistTokenView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def login_request(request):

#     if request.user.is_authenticated:
#         return redirect("index")

#     if request.method == 'GET':
#         # GET isteği geldiğinde oturum açma formunu döndür
#         form = LoginUserForm()
#         return render(request, 'account/login.html', {'form': form})

#     elif request.method=="POST":
#         form=LoginUserForm(request, data=request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             user=authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)

#                 # JWT tokenleri oluştur ve dön
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'access_token': str(refresh.access_token),
#                     'refresh_token': str(refresh),
#                 })
#             else:
#                 return render(request, 'account/login.html', {'form': form})

#         return render(request, 'account/login.html', {'form': form})
#     else:
#         form=LoginUserForm()
#         return render(request, 'account/login.html', {'form': form})


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def register_request(request):

#     if request.method == 'GET':
#         # GET isteği geldiğinde kayıt formunu döndür
#         form = NewUserForm()
#         return render(request, 'account/register.html', {'form': form})

#     elif request.method=="POST":
#         form=NewUserForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password1"]
#             user=authenticate(username=username, password=password)
#             login(request, user)
            
#             # JWT tokenleri oluştur ve dön
#             #yenileme token'ı anlamına gelir. Bu token, geçerli bir access token'ın süresi dolduğunda kullanıcının oturumunun kesilmeden (logout olmadan) devam edebilmesini sağlar.
#             refresh = RefreshToken.for_user(user) #JSON formatında bir yanıt döndürür.
#             return Response({
#                 'access_token': str(refresh.access_token), #kullanıcının işlemlerini gerçekleştirmesi için kullanılır.
#                 'refresh_token': str(refresh),
#             })
#         else:
#             return render(request, "account/register.html", {"form":form})
        
#     form=NewUserForm()
#     return render(request, "account/register.html", {"form":form})

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_request(request):
#     logout(request)
#     return redirect("index")

#     # if request.method == 'POST':
#     #     refresh_token = request.data.get('refresh_token')
#     #     if not refresh_token:
#     #         return Response({'error': 'Refresh token not provided'}, status=400)

#     #     try:
#     #         token = RefreshToken(refresh_token)
#     #         token.blacklist()  # JWT token'ı geçersiz hale getir
#     #         return Response({'detail': 'Successfully logged out.'}, status=200)
#     #     except Exception as e:
#     #         return Response({'error': 'Invalid refresh token'}, status=400)

        


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        token = response.data["access"] # NEW LINE

        response.set_cookie('token', token, httponly=True)
        return response