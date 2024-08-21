from django.urls import path
from postapp import views


urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('insert/',views.create_post,name='create_post'),
    path('update/<int:id>/',views.update_post,name='update_post'),
    path('delete/<int:id>/',views.delete_post,name='delete_post'),
    path('signup/',views.signup_view,name='signup'),
]