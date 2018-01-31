#imported forms module
from django import forms
from django.contrib.auth import get_user_model

#defining user model from django user model module
User = get_user_model()

#form definition and validation for contact form
class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your message"}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Only google user can do this.")
		return email

#form definition and validation for login form
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

#form definition and validation for register form
class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		queryset = User.objects.filter(username=username)
		if queryset.exists():
			raise forms.ValidationError("This username has already taken.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		queryset = User.objects.filter(email=email)
		if queryset.exists():
			raise forms.ValidationError("This email has already taken.")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Use the same password")
		return data		