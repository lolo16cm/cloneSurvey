from api import views as api_views
from django.urls import path
#access token expires quickly, refresh token allow longer access(which can get the new access when old one is expired with no additinal login)
from rest_framework_simplejwt.views import TokenRefreshView

#as_view() is used for cbv
urlpatterns = [
    path('user/token/', api_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/',api_views.RegisterView.as_view()),
]