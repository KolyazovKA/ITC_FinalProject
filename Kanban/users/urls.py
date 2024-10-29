from django.urls import path
from users.views import UserDetail

urlpatterns = [
    path('user/<int:pk>', UserDetail.as_view(), name='user_profile')
]