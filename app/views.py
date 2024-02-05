from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING',mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by('sal')
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by('-sal')
    EMPOBJECTS=Emp.objects.select_related('deptno').order_by(Length('ename').desc())
    EMPOBJECTS=Emp.objects.select_related('deptno').exclude(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    


    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal=2500)
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)






def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    emd=Emp.objects.select_related('deptno','mgr').all()
   
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):
    EO=Emp.objects.all()
    SO=SalGrade.objects.all()
    # Retrieving the data of employess who belongs to grade 4
    SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
   











    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)