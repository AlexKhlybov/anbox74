import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView

from apps.product.models import Boiler


class BoilerDetailView(DetailView):
    model = Boiler
    template_name = "product/product_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "AnBox74 | Детали продукта"
        return context
