from django.template import loader
from django.http import HttpResponse


def members(request):
    template = loader.get_template("user/index.html")
    return HttpResponse(template.render())
