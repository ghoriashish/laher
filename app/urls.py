from django.urls import path,include
from . import views
urlpatterns = [
    
    ## *****************Page Urls******************
    path("",views.RegisterPage,name="register"),
    path("sucess/",views.SucessPage,name="sucess"),
    path("showdata/",views.ShowPage,name="showdata"),
    path("js/",views.JSPage,name="js"),




    ## ***************Action Views(After Submit)****************
    path("register/",views.RegisterUser,name="registeruser"),
    path("show_details/",views.show_details,name="showdetails"),
]
