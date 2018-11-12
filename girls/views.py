# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.views.generic import TemplateView
from girls.models import Girl
from girls.forms import SearchForm
from datetime import datetime, timedelta


class GirlsListView(FormView):

    model = Girl
    template_name = "girls/girls_list.html"
    form_class = SearchForm

    def form_valid(self, form):

        age_from = form.cleaned_data['age_from']
        age_to = form.cleaned_data['age_to']

        hair_color = form.cleaned_data['hair_choice']
        print(hair_color)

        girls = Girl.objects

        if age_from is not None:
            date_from = datetime.now() - timedelta(age_from*366)
            girls = girls.filter(date_of_birth__lte=date_from)
        if age_to is not None:
            date_to = datetime.now() - timedelta(age_to * 366)
            girls = girls.filter(date_of_birth__gte=date_to)
        if hair_color is not None and hair_color != 'All':
            girls = girls.filter(hair_color=hair_color)

        print("LEN", len(girls.filter(has_cover=True).all()))

        return render(self.request, self.template_name, {'form': form,
                                                         'girls': girls.all()})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['girls'] = Girl.objects.all()

        return context


class GirlDetailView(TemplateView):
    template_name = "girls/girl_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = int(self.kwargs['id'])
        context['girl'] = Girl.objects.get(id=id)

        return context
