from django import forms
from .models import Student



class Student_Form(forms.ModelForm):

	class Meta:
		model = Student
		fields = '__all__'

class Update_Form(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'age', 'faculty', 'department', 'about']