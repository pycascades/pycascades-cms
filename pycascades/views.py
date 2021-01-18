from bakery.views import BuildableTemplateView


class Buildable404View(BuildableTemplateView):
    build_path = '404.html'
    template_name = '404.html'