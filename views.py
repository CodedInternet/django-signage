from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import generic

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'signage/index.html'

# Custom logon class to redirect to the previous page
def login(request, **kwargs):
    if request.user.is_authenticated():
        next = request.REQUEST.get('next', '/')
        return HttpResponseRedirect(request.REQUEST.get('next', '/'))
    else:
        from django.contrib.auth.views import login

        return login(request)
