from django.views.generic import ListView, TemplateView

from apps.news.models import News
from apps.main.models import Delivery, Payments
from apps.product.models import Boiler


class HomePageList(ListView):
    model = News
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Главная"
        context["boiler"] = Boiler.objects.filter(is_active=True)
        return context

class ContactPageList(ListView):
    model = News
    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Контакты"
        return context

class DeliveryPageList(ListView):
    model = Delivery
    template_name = "main/delivery.html"
    context_object_name = 'delivers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Доставка"
        return context

class PaymentsPageList(ListView):
    model = Payments
    template_name = "main/payments.html"
    context_object_name = 'payments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Оплата"
        return context


class RobotsTxtew(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SitemapXmlView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivery'] = Delivery.objects.all()
        context['payments'] = Payments.objects.all()
        context['news'] = News.objects.all()
        context['boiler'] = Boiler.objects.filter(is_active=True)
        return context
