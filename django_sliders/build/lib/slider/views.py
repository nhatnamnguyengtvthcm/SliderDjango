import json

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django_sliders.slider.models import Slider
from django_sliders.slider.serializers import SliderTemplate


class SliderIndex(TemplateView):
    template_name = "index.html"

    def get(self, request):

        sliders = Slider.objects.all()

        serializers = SliderTemplate(sliders, many = True)

        slider_data = json.loads(json.dumps(serializers.data))
        context = { "sliders": sliders, "slider_data": slider_data}

        return render(request, self.template_name, context)