from django.conf.urls import url
from basic_app import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
