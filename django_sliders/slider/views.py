from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django_sliders.slider.models import Slider


class SliderIndex(TemplateView):
    template_name = "index.html"

    def get(self, request):
        sliders = Slider.objects.all()
        context = { "sliders": sliders }

        return render(request, self.template_name, context)