from.import views
from django.urls import path,include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('',views.demo,name='remo')
    #path('add/',views.addition,name='addition')


    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('details/',views.details,name='details'),
    #path('thanks/',views.thanks,name='thanks')
]