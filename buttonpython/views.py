from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
def button(request):
    return render(request,'index.html')
def output(request):
    print("Hello world!")
    data="Hello world!"
    return render(request,'index.html',{'data': data})
def external(request):
    out=run([sys.executable,'//home//ankit//projects6thsem//hci//Mouse_Cursor_Control_Handsfree-master//mouse-cursor-control.py'],shell=False,stdout=PIPE)
    return render(request,'index.html')
    