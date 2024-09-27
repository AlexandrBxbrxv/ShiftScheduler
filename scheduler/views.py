from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'scheduler/home.html'
