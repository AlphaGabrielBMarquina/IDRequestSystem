
from re import template
from xml.etree.ElementInclude import include
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import MyPasswordChangeForm
from . import views     

#urlconf
urlpatterns = [
    path('', views.login1, name='login'),
    path('loginprocess/', views.loginto, name='loginto'),
    path('logout/', views.gotologout, name='gotologout'),
    path('sidregistration/', views.sidreg, name='sidreg'),
    path('fidregistration/', views.fidreg, name='fidreg'),
    path('coid/', views.coid, name='coid'),
    path('pdfcreations/<str:pk>/', views.pdfcreations, name='pdfcreations'),
    path('pdfcreationf/<str:pk>/', views.pdfcreationf, name='pdfcreationf'),
    path('approval/', views.approval, name='approval'),
    path('approvesa/<int:id>', views.approvesa, name='approvesa'),
    path('approvalf/', views.approvalf, name='approvalf'),
    path('approvefa/<int:id>', views.approvefa, name='approvefa'),
    path('userreg/', views.userreg, name='userreg'),
    path('loginto/', views.loginto, name='loginto'),
    path('changepass/', views.changepass, name='changepass'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('deletef/<str:pk>/', views.deletef, name='deletef'),
    path('dones/<str:pk>/', views.dones, name='dones'),
    path('donef/<str:pk>/', views.donef, name='donef'),
    path('sview/<str:pk>/', views.sview, name='sview'),
    path('fview/<str:pk>/', views.fview, name='fview'),
    path('update/<str:pk>/', views.update, name='update'),
    path('updatef/<str:pk>/', views.updatef, name='updatef'),
    path('changepassword/', 
        PasswordChangeView.as_view(
            template_name='Final html/change_password.html',
            success_url=reverse_lazy('password_change_done'),
            form_class=MyPasswordChangeForm
        ), 
        name='password_change'),
    path('changepassword/done/', 
        PasswordChangeDoneView.as_view(
            template_name='Final html/password_change_done.html',
        ), 
        name='password_change_done'),
]