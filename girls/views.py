# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from girls.models import Girl


class GirlsListView(ListView):

    model = Girl

    #paginate_by = 100  # if pagination is desired
    template_name = "girls/girls_list.html"

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
