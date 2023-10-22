from django.urls import path,include
from .views import *


urlpatterns = [
   path('login/', login_page, name = 'login'),
   path('logout/', logout_f, name = 'logout'),

   path('register/', register_page, name = 'register'),
   path('account/', account, name = 'account'),

]