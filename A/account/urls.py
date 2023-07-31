from django.urls import path
from . import views

#این app_name باید هم نام namespaceدر url اصلیمان باشد
app_name = 'account'
urlpatterns = [
        path('register/', views.UserRegisterView.as_view(), name = 'user_register'),
]