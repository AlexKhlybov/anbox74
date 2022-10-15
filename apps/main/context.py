from apps.main.models import SiteConfiguration


def get_config(request):
    """Пробрасывает конфиг сайта"""
    config = SiteConfiguration.get_solo()
    return {"site_config": config,}
