from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
	context = {
		"title": "Hello World!",
		"content": "Welcome to home page."
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title": "About Page!",
		"content": "Welcome to about page."
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)

	context = {
		"title": "Contact Page!",
		"content": "Welcome to contact page.",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/view.html", context)
