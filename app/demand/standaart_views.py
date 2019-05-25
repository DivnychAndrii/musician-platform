from django.shortcuts import render
from django.views import View


class Demand(View):
    template = 'demand.html'

    def get(self, request):
        return render(request, self.template, )
