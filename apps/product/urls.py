from django.urls import path

from apps.product import views as product

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', product.BoilerDetailView.as_view(), name='detail_product'),
]