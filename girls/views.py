from django.shortcuts import render
from django.views.generic.list import ListView
from girls.models import Girl


class GirlsListView(ListView):

    model = Girl

    #paginate_by = 100  # if pagination is desired
    template_name = "girls/models.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context