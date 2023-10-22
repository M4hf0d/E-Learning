from django.urls import path,include
from .views import *


urlpatterns = [

   # path('', index, name = 'index'),
    path('', homepage, name = 'homepage'),
    path('courses/<int:pk>', CoursesView, name = 'course_page'),
    path('assignements/<int:pk>', AssginementsView, name = 'assignements_page'),
    path('submit-assignments/<int:pk>', project_submission , name='Submit_assignments'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
 
 ]



