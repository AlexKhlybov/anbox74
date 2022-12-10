from django.urls import path

from apps.main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.HomePageList.as_view(), name='index'),
    path('contact/', main.ContactPageList.as_view(), name='contact'),
    path('delivery/', main.DeliveryPageList.as_view(), name='delivery'),
]