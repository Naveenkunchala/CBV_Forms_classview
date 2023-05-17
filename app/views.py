from django.shortcuts import render

from django.views.generic import FormView

from django.http import HttpResponse

from app.forms import *

# Create your views here.


class CBV_form(FormView):
    template_name='CBV_form.html'
    form_class=SchoolForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('Data Inserted Sucessfully')


