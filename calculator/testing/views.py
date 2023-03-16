from django.http import HttpResponse
from django.template import loader
from .models import Testing


def members(request):
    members = Testing.objects.all().values()
    template = loader.get_template("for_in.html")
    context = {
        "db": members,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    members = Testing.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "db": members,
    }
    return HttpResponse(template.render(context, request))
