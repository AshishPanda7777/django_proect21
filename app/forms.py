from  django import forms 

class Student_form(forms.Form):
    sname=forms.CharField(max_length=20)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    spassword=forms.CharField(widget=forms.PasswordInput)