from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', BookingView.as_view(), name='booking-list'),
    path('api-token-auth/', obtain_auth_token),
]