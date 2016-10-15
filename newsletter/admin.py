from django.contrib import admin

# Register your models here.

#from someotherapp.models import someothermodel
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display=["__str__","time_stamp","updated"]
	form =SignUpForm
	#class Meta:
	#	model=SignUp



admin.site.register(SignUp,SignUpAdmin)