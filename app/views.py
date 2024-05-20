from django.shortcuts import render

# Create your views here.
from app.forms import  *
def school(request):
    ESFO=Student_form()
    d={'ESFO':ESFO}
    return  render(request,'school.html',d)