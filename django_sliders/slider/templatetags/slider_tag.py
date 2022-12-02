from django_sliders.slider.models import Slider
from django import  template

register = template.Library()

@register.inclusion_tag('slider_list.html')
def render_slider():
    sliders = Slider.objects.all()
    print(sliders)
    for slider in sliders:
        print(slider.slider_img)
        print(slider.slider_img.url)
        print(slider.slider_img.path)
    return {
        "sliders": sliders
    }
