from django.urls import path

from apps.main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.HomePageList.as_view(), name='view_list'),
]