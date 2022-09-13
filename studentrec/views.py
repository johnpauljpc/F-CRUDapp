from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.views.generic import DetailView
from .forms import Student_Form, Update_Form
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


######### View for the home-page #############
def ListView(request):
	students = Student.objects.all().order_by('-id')
	context = {'students':students}
	return render(request, 'home.html', context)



############ CREATE FUNCTIONALITY ##################
def CreateView(request):
	form = Student_Form()
	if request.method == 'POST':
		form = Student_Form(request.POST)
		
		if form.is_valid():
			new_user = form.cleaned_data.get('name')
			form.save()
			messages.success(request, "Created a new student's record for " + new_user )
			return redirect('home')
	context = {'form': form}
	
	return render(request, 'create.html', context)


############ READ/detail-view FUNCTIONALITY ###########
def DetailView(request, reg_no):
	students = Student.objects.get(reg_no = reg_no)
	context = {
	'students':students
	}

	return render (request, 'details.html', context)


############ UPDATE FUNCTIONALITY ##################

def UpdateView(request, reg_no):
	#obj = get_object_or_404(Student, reg_no = reg_no)
	obj = Student.objects.get(reg_no = reg_no)
	form = Update_Form(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		usr = form.cleaned_data['name']
		messages.info(request, 'updated record for ' + usr)
		return HttpResponseRedirect(reverse('detail', args=[str(reg_no)]))
	
	context = {'form':form}

	return render(request, 'update.html', context) 

############ DELETE FUNCTIONALITY ##################
def DeleteView(request, reg_no):
	record = get_object_or_404(Student, reg_no =reg_no)
	usr = record.name

	if request.method == 'POST':
		record.delete()
		messages.info(request, 'record for ' + usr + ' is deleted')
		return redirect('home')

	return render(request, 'delete.html' )


################### THE END ##########################

