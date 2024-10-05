from django.urls import path
from django.contrib import admin 
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',log_in, name="log_in"),
    path('log_in',log_in, name="log_in"),
    path('register', register, name="register"),
    path('AgentRegister', AgentRegister, name="AgentRegister"),
    path('home',home, name="home"),
    path('loginToSignUp', loginToSignUp, name="loginToSignUp"),
    path('signUpTologin', signUpTologin, name="signUpTologin" ),
    path('toAgentSignUp', toAgentSignUp, name="toAgentSignUp" ),
    path('productDetails/<int:pk>',productDetails, name="productDetails"),
    path('redirect-to-productDetails/<int:pk>', productDetails, name='redirect_to_productDetails'),
    path('search', search,name="search"),
    path('category/<str:cid>',category, name="category"),
    path('pricerange/<str:prid>',pricerange, name="pricerange"),
]