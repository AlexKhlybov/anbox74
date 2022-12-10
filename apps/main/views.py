from django.views.generic import ListView

from apps.news.models import News
from apps.main.models import Delivery
from apps.product.models import Boiler


class HomePageList(ListView):
    model = News
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Главная"
        context["boiler"] = Boiler.objects.all()[:6]
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
