from django.urls import path, include
from .views import index,home,department_info,all_patients,search

app_name = 'usermanagement'

urlpatterns = [
    path('', index , name="index"),
    path('home/', home , name="home"),
    path('<name>/info/', department_info, name="department_info"),
    path('all_patients/', all_patients , name="all_patients"),
    path('search/', search , name="search"),

]