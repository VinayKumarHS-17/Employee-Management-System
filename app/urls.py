from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('edit_emp/<int:id>/',edit_emp,name='edit_emp'),
    path('delete_emp/<int:id>/',delete_emp,name='delete_emp')
]
