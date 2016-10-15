from django.shortcuts import render

from .forms import SignUpForm
# Create your views here.
def home(request):

	title ="Welcome"
	# if request.user.is_authenticated():
	# 	title="My title %s "%(request.user) 
	#add a form
	form= SignUpForm()
	context = {
		"template_title" : title,
		"form":form,
	}
	return render(request,'home.html',context)	
