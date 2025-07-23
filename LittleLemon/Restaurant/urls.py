from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingView

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', BookingView.as_view(), name='booking-list'),
]