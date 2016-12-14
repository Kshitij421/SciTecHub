from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm,SignUpForm
# Create your views here.
# def home(request):

# 	title ="Welcome"
# 	# if request.user.is_authenticated():
# 	# 	title="My title %s "%(request.user) 
# 	#add a form
# 	# if request.method=="POST":
# 	# 	print request.POST

# 	form= SignUpForm(request.POST or None)
# 	context = {
# 		"template_title" : title,
# 		"form":form,
# 	}
# 	if form.is_valid():
# 		#form.save()
# 		instance=form.save(commit=False)
# 		if not instance.full_name:
# 			instance.full_name="AnonymousUser"
# 		instance.save()

# 		#print( instance)
# 		# print (instance.email)
# 		# print (instance.time_stamp)
# 		context={
# 			"template_title": "ThankYou! %s"%(instance.full_name),
# 			form:""
# 		}


	
	# return render(request,'home.html',context)	

def home(request):
	return render(request,'index.html',{})

def contact(request):
	title="Contact Form"

	form=ContactForm(request.POST or None)

	context={
	"template_title":title,
	"form":form,
	}
	if form.is_valid():

		form_email=form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")
		# print (email,message,full_name)

		# for key in form.cleaned_data:
		# 	print (key,":",form.cleaned_data.get(key))


		# for key,value in form.cleaned_data.items():
		# 	print (key,":",value)
		subject=" Testing Email Sending"
		contact_message="%s:%s via %s "%(
			form_full_name,
			form_message,
			form_email)

		from_email=settings.EMAIL_HOST_USER
		to_email="kshitijwarungase@gmail.com , ameychaudhary1@gmail.com"
		#message=("Hello I'm %s")%full_name
		some_html_message="""
		<h1>Hello</h1>
		"""

		send_mail(subject,
			contact_message,
			from_email,
			[to_email],
			html_message=some_html_message,
			fail_silently=False)

	return render(request,'contactform.html',context	)