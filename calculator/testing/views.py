from django.http import HttpResponse
from django.template import loader
from .models import Testing


def members(request):
    members = Testing.objects.all()
    template = loader.get_template("for_in.html")
    context = {
        "db": members,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    members = Testing.objects.get(slug=slug)
    template = loader.get_template("details.html")
    context = {
        "db": members,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
