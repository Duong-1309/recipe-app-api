from django.urls import path

from user.views import set_data_views


app_name = 'user'

urlpatterns = [
    path('create/', set_data_views.CreateUserView.as_view(), name='create'),
    path('token/', set_data_views.CreateTokenView.as_view(), name='token'),
]
