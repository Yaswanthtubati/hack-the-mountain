from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('Homep',views.Homep,name="Homep"),
    path('Hospitals',views.Hospitals,name="Hospitals"),
    path('diet',views.diet,name="diet"),
    path('cp/',views.cp),
    path('cp/cp1',views.cp1),

    path('explore',views.explore,name="explore"),
    path('prediction/',views.prediction),
    path('prediction/prediction1',views.prediction1),
    path('Ananthapur',views.Ananthapur,name="Ananthapur"),
    path('Chittoor',views.Chittoor,name="Chittoor"),
    path('EastGodhavari',views.EastGodhavari,name="EastGodhavari"),
    path('Guntur',views.Guntur,name="Guntur"),
    path('Kadapa',views.Kadapa,name="Kadapa"),
    path('Krishna',views.Krishna,name="Krishna"),
    path('Kurnool',views.Kurnool,name="Kurnool"),
    path('Nellore',views.Nellore,name="Nellore"),
    path('Prakasam',views.Prakasam,name="Prakasam"),
    path('Srikakulam',views.Srikakulam,name="Srikakulam"),
    path('Vijayanagaram',views.Vijayanagaram,name="Vijayanagaram"),
    path('Visakhapatnam',views.Visakhapatnam,name="Visakhapatnam"),
    path('WestGodhavari',views.WestGodhavari,name="WestGodhavari"),

]
