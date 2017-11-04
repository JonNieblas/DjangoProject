from django.http import HttpResponse
from .models import Section
from .models import Course
from .models import Professor

from django.shortcuts import get_object_or_404, render

def index(request):
    html = "<h1>Welcome!</h1>" + '<br><strong><a href="/register/section/">Sections</a></strong>' + '<br><strong><a href="/register/professor/">Professors</a></strong>' + '<br><strong><a href="/register/course/">Courses</a></strong>'
    return HttpResponse(html)

def section(request):
    section_list = Section.objects.all()
    context = {
        'section_list': section_list,
    }
    return render(request, 'register/section.html', context)

def section_detail(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'register/section_detail.html', {'section': section})

def course(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list,
    }
    return render(request, 'register/course.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'register/course_detail.html', {'course': course})

def professor(request):
    professor_list = Professor.objects.all()
    context = {
        'professor_list': professor_list,
    }
    return render(request, 'register/professor.html', context)

def professor_detail(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    return render(request, 'register/professor_detail.html', {'professor': professor})