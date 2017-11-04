from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #ex: /register/section
    url(r'^section/$', views.section, name='section_page'),
    #ex: /register/section/1
    url(r'^section/(?P<section_id>[0-9]+)/$', views.section_detail, name ='section_detail'),

    #ex: /register/course
    url(r'^course/$', views.course, name='course_page'),
    # ex: /register/course/1
    url(r'^course/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),

    #ex: /register/professor
    url(r'^professor/$', views.professor, name='professor_page'),
    # ex: /register/professor/1
    url(r'^professor/(?P<professor_id>[0-9]+)/$', views.professor_detail, name='professor_detail'),

]