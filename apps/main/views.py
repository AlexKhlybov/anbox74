from django.shortcuts import render
from django.views.generic import ListView

# from apps.companies.models import Company
from apps.news.models import News
from apps.product.models import Boiler
# from apps.resume.models import Resume, ResumeFavorites
# from apps.vacancies.models import Vacancy, VacancyFavorites


class HomePageList(ListView):
    model = News
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Anbox74 | Главная"
        context["boiler"] = Boiler.objects.all()[:6]
        return context
