from django.urls import path

#from . import views
from .views import addPatronView, index, userDetailsView, userHomeView\
    , loginView, loginFormView, patronManagerView, patronFormView\
        , addNumberView, logoutView, logoutFormView

urlpatterns = [
    path('', index, name='home'),
    path('patronmanager/', patronManagerView, name='patron-manager'),
    path('loginForm/', loginFormView, name='loginform'),
    path('logoutForm/', logoutFormView, name='logoutform'),
    path('patronForm/', patronFormView, name='patronform'),
    
    path('loginForm/login/', loginView, name='login'),
    path('logoutForm/logout/', logoutView, name='logout'),
    path('patronForm/newpatron/', addPatronView, name='newpatron'),
    path('patrons/<username>/addnumber/', addNumberView, name='addnum'),

    path('patrons/<username>/', userDetailsView, name='user-detail'),
    
]