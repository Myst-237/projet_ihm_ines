from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

# Create your views here.

def search(request):
    patients = []
    role = request.GET.get('role')
    if request.method == 'POST':
        search = request.POST.get('search')
        if search is not None:
            users = CustomUser.objects.filter(Q(username__icontains=search) | Q(first_name__icontains=search) | Q(last_name__icontains=search))
            if len(users) > 0:
                for user in users:
                    try:
                        patients.append(Patient.objects.get(user=user))
                    except ObjectDoesNotExist:
                        pass
                if len(patients) == 0:
                        messages.info(request, "Patient with Name '"+ search + "' does not exist")
                        return redirect('usermanagement:home')
                else:
                    context = {'patients': patients,
                               }
                    return render(request, "usermanagement/patients.html",context)
                    
            else:
                messages.info(request, "Patient with Name '"+ search + "' does not exist")
                return redirect('usermanagement:home')
        else:
            messages.info(request, "Please enter a keyword to search")
            return redirect('usermanagement:home')
    
    messages.info(request, "Please enter a keyword to search")
    return redirect('usermanagement:home')

def index(request):
    return render(request, 'usermanagement/index.html')

def home(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'usermanagement/home.html', context)


def department_info(request, name):
    return render(request, 'usermanagement/'+name+'.html',)

def all_patients(request):
    context = {
        'patients': Patient.objects.all().order_by('-created')
    }
    return render(request, 'usermanagement/patients.html', context)