# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
# from django.contrib.auth.models import User
# from django import forms
# # from django.utils.translation import getext, gettext_lazy as _

# # Student_Signup_Form
# class Student_Signup_Form(UserCreationForm):
#     password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email']
#         labels={'email':'Mail Id'}
#         widgets = {
#             'username':forms.TextInput(attrs={'class':'form-control'}),
#             'first_name':forms.TextInput(attrs={'class':'form-control'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'}),
      
#         }

# # user_login_form
# class User_Login(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs=
#     {'autofocus':True, 'class':'form-control'}))

#     password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(attrs=
#     {'autocomplete':'current-password', 'class':'form-control'}))
