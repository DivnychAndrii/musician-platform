from django.shortcuts import render
from django.views import View


class AllLessons(View):
    template = 'lessons.html'

    def get(self, request):
        return render(request, self.template, )
