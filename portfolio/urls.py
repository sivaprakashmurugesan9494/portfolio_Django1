from django.urls import path
from . import views
urlpatterns=[path("homepage/",views.homepage,name='homepage'),
             path("login/",views.login,name='login'),
             path("signup/",views.signup,name='signup'),
            path("index/",views.index,name='index'),

]