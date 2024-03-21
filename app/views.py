from django.shortcuts import render,redirect,HttpResponse
from .models import Student_details,Marks

def home(request):
    data=Student_details.objects.all()
    return render(request,"index.html",{'key':data})

def students(request):
    name = request.POST.get("name")    
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    roll_no =request.POST.get("roll_no")
    city = request.POST.get("city")
    ob=Student_details(
        name=name,
        phone=phone,
        email=email,
        roll_no=roll_no,
        city=city,
    )
    ob.save()
    return redirect("/")

def marks(request,eid):    
    students = Student_details.objects.get(id=eid)
    records = Marks.objects.filter(students=students)
    print(records)
    

def delete(request):
    sid = request.GET.get('sid')
    obj = Student_details.objects.get(id=sid)
    obj.delete()
    return redirect("/")

def updateStudents(request):
    print(request.method)
    if request.method=="GET":
        sid = request.GET.get('sid')
        obj = Student_details.objects.get(id=sid)    
        return render(request,"update.html",{"student":obj})
    else:
        student_obj = Student_details()
       
    student_obj.name = request.POST.get('name')    
    student_obj.phone = request.POST.get("phone")
    student_obj.email = request.POST.get("email")
    student_obj.roll_no =request.POST.get("roll_no")
    student_obj.city = request.POST.get("city")
    print(student_obj)
    student_obj.save() 
    return redirect("/")

def search(request):
    query = request.GET.get('query')
    results=[]
    if query:
        results = Student_details.objects.filter(student_details_name__icontains=query)
        return render(request, "index.html", {results})
    else:
        return HttpResponse("not found")
