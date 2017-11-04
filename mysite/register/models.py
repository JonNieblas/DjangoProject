from django.db import models

class Course(models.Model):
    #only requires name for now
    course_name = models.CharField(max_length=20)

    #allows for easy visual of individual course names
    def __str__(self):
        return self.course_name

class Professor(models.Model):
    #only reguires name for now
    professor_name = models.CharField(max_length=20)

    # allows for easy visual of individual professor names
    def __str__(self):
        return self.professor_name

class Section(models.Model):
    section_name = models.CharField(max_length=4)

    #allows for usage of professor names during section creation
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    #allows for usage of course names during section creation
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    #the number of credits of a section is defaulted at 3. Can be changed if desired.
    credits = models.IntegerField(default=3)

    # allows for easy visual of individual section names
    def __str__(self):
        return self.section_name