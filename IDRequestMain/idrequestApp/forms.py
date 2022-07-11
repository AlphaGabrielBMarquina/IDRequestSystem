from re import A
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Useraccount, registration, Fregistration
from django.core.mail import send_mail

class Userreg(UserCreationForm):
    class Meta:
        model = Useraccount
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'Usertype']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'Usertype' : forms.Select(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }

        # or fields = __all__'

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}
            
class registerist(ModelForm):
    class Meta:
        model = registration
        fields = ['firstname1','middlename','lastname','course','conterpersonn', 'contactnum', 'address','studnum', 'imagee', 'signature', 'semail']
        widgets ={
            'firstname1' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'middlename' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'course' : forms.Select(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'conterpersonn'  : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'contactnum' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'address' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'studnum' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'semail' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2','placeholder': 'Enter Your Email Address You Used In Login'}),
            }

    def save(self):
        user1 = super().save(commit=False)
        user1.semail = self.cleaned_data.get('semail')
        user1.firstname1 = self.cleaned_data.get('firstname1')
        user1.lastname = self.cleaned_data.get('lastname')

        user1.save()

        send_mail('Registration Successful',
            f"""Congratulations! {user1.firstname1} {user1.lastname}
            Your ID Request Has Been Successfully Submitted. Please Wait for the Approval Process.\n
        """+ '\n'+"Thank You",
            
            'tupcuitc.idreq@gmail.com',
            [f'{user1.semail}'],
            fail_silently=False)

        return user1


class fregisterist(ModelForm):
    class Meta:
        model = Fregistration
        fields = ['Ffirstname1','Fmiddlename','Flastname','Femployeenum','Fgsis','Fgsisno','Ftin','Fpagibig','Fphilhealth','Fothers','Fconterpersonn', 'Fcontactnum', 'Faddress', 'Fimagee', 'Fsignature', 'femail']
        widgets ={
            'Ffirstname1' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fmiddlename' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Flastname' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Femployeenum' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),

            'Fgsis' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fgsisno' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Ftin' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fpagibig' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fphilhealth' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fothers' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),



            'Fconterpersonn'  : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Fcontactnum' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'Faddress' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            'femail' : forms.TextInput(attrs={'class':'form-control mb-4 mr-sm-2'}),
            
        }
    def save(self):
        user2 = super().save(commit=False)
        user2.femail = self.cleaned_data.get('femail')
        user2.Ffirstname1 = self.cleaned_data.get('Ffirstname1')
        user2.Flastname = self.cleaned_data.get('Flastname')
        user2.save()

        send_mail('Registration Successful',
            f"""Congratulations! {user2.Ffirstname1} {user2.Flastname}
            .Your ID Request Has Been Successfully Submitted. Please Wait for the Approval Process.\n
        """,
            
            'tupcuitc.idreq@gmail.com',
            [f'{user2.femail}'],
            fail_silently=False)

        return user2