from django.shortcuts import render
from django.views import View


class AllLessons(View):
    template = 'lessons.html'

    def get(self, request):
        return render(request, self.template, )


class OneLesson(View):
    template = 'onelesson.html'

    def get(self, request, **kwargs):
        lesson_id = kwargs['lesson_id']
        context = {
            'lesson_id': lesson_id,
        }
        return render(request, self.template, context)
