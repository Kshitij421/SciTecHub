from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp

		fields=['full_name','email']
		####exclude=['full_name']

	def clean_email(self):

		email=self.cleaned_data.get('email')
		email_base,provider=email.split('@')
		domain,extension=provider.split('.')

		# if not domain =="gmail":
		# 	raise forms.ValidationError("Please Your Gmail Email Address")
		if not extension =="edu":
			raise forms.ValidationError("Please Use A Valid College (.edu) Email Address")

		#if not "edu" in email:
		#	raise forms.ValidationError("Please Use a Valid College (.edu ) Email Address")
		return email

	def clean_full_name(self):
		full_name=self.cleaned_data.get('full_name') 
		return full_name
