from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserRegisterView, UserDetailView
from contacts.views import ContactListCreateView, ContactDetailView, SpamReportCreateView
from .views import index  # Import the index view

urlpatterns = [
    path('', index, name='index'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('api/register/', UserRegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserDetailView.as_view(), name='user_detail'),
    path('api/contacts/', ContactListCreateView.as_view(), name='contact_list_create'),
    path('api/contacts/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('api/spam/', SpamReportCreateView.as_view(), name='spam_report'),
]
