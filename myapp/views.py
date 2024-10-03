from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import EmployeeForm
from myapp.models import Emplpoyee
from django.contrib import messages


class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):
        
        form_instance=EmployeeForm()
        
        return render(request,"employee_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Emplpoyee.objects.create(**data)

            messages.success(request,"added succesfully")

            return redirect("Employee_list")

        else:

            messages.error(request,"update failed")



            return render(request,"employee_create.html",{"form":form_instance})

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Emplpoyee.objects.all()

        return render(request,"employee_list.html",{"Employee":qs})

class EmplpoyeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Emplpoyee.objects.get(id=id)

        return render(request,"employee_detail.html",{"Employee":qs})

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Emplpoyee.objects.get(id=id).delete()
        
        return redirect("Employee_list")



class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_obj=Emplpoyee.objects.get(id=id)

        employee_dictionary={

            "name":employee_obj.name,
            "designation":employee_obj.designation,
            "department":employee_obj.department,
            "salary":employee_obj.salary,
            "contact":employee_obj.contact,
            "address":employee_obj.address,

        }

        form_instance=EmployeeForm(initial=employee_dictionary)

        return render(request,"employee_update.html",{"form":form_instance})


    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Emplpoyee.objects.filter(id=id).update(**data)

            return redirect("Employee_list")

        else:

            return render(request,"employee_update.html",{"form":form_instance})


