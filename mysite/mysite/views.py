from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'mysite/main.html'
