from django.urls import path
from auth_test.views import *
urlpatterns = [
    path('', TestView.as_view(), name='auth_test')
]