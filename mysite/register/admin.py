from django.contrib import admin

from .models import Professor
from .models import Course
from .models import Section

#only admin has auth/z to create professors
admin.site.register(Professor)

#only admin has auth/z to create courses
admin.site.register(Course)

#only admin has auth/z to create sections
admin.site.register(Section)
