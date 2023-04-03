from django.urls import path

from apps.main import views as main

from django.views.generic.base import TemplateView


app_name = 'main'

urlpatterns = [
    path('', main.HomePageList.as_view(), name='index'),
    path('contact/', main.ContactPageList.as_view(), name='contact'),
    path('delivery/', main.DeliveryPageList.as_view(), name='delivery'),
    path('payments/', main.PaymentsPageList.as_view(), name='payments'),
    path("robots.txt", main.RobotsTxtew.as_view()),
    path("sitemap.xml", main.SitemapXmlView.as_view()),
]