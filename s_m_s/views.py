from django.shortcuts import render
from s_m_s.models import *
from django.http import HttpResponse

# Create your views here.
def view_student(request):
    if request.method=='GET':
        resp=render(request,'s_m_s/index.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            smp=Student()
            smp.name=request.POST.get('txtname','NA')
            smp.age=request.POST.get('txtage',0)
            smp.rollno=request.POST.get('txtroll',0)
            smp.course=request.POST.get('txtcourse','NA')
            smp.email=request.POST.get('txtemail','NA')
            smp.address=request.POST.get('txtaddress','NA')
            smp.save()
            resp=HttpResponse("<h1>Data Inserted SuccessFully!! Whose ID is "+str(smp.id)+"</h1>")
            return resp

        elif 'btnsearch' in request.POST:
            smpid=int(request.POST.get('txtid',0))
            smp=Student.objects.get(id=smpid)
            d1={'smp':smp}
            resp=render(request,'s_m_s/index.html',context=d1)
            return resp

        # elif 'btnsearch' in request.POST:
        #     cmpid=int(request.POST.get('txtid',0))
        #     print(cmpid)
        #     cmp=Student.objects.get(id=cmpid)
        #     d1={'cmp':cmp}
        #     resp=render(request,'s_m_s/index.html',context=d1)
        #     return resp 
            
        elif 'btnupdate' in request.POST:
            smp=Student()
            smp.id=int(request.POST.get('txtid',0))
            if Student.objects.filter(id=smp.id).exists():
                 smp.name=request.POST.get('txtname','NA')
                 smp.age=request.POST.get('txtage',0)
                 smp.rollno=request.POST.get('txtroll',0)
                 smp.course=request.POST.get('txtcourse','NA')
                 smp.email=request.POST.get('txtemail','NA')
                 smp.address=request.POST.get('txtaddress','NA')
                 smp.save()
                 resp=HttpResponse("<h1>Data Updated SuccessFully!! Whose ID is "+str(smp.id)+"</h1>")
                 return resp

        elif 'btndelete' in request.POST:
            smp=Student()
            smp.id=int(request.POST.get('txtid',0))
            if Student.objects.filter(id=smp.id).delete():
                resp=HttpResponse("<h1>Data Deleted SuccessFully!! Whose ID is "+str(smp.id)+"</h1>")
                return resp

        elif 'btnshow' in request.POST:
            allsmp=Student.objects.all()
            d1={'allsmp':allsmp}
            resp=render(request,'s_m_s/index.html',context=d1)
            return resp



