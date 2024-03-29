from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic
from django.core.mail import send_mail
from django.conf import settings

from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you! I will be in touch soon!')
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		print(form.cleaned_data)
		send_mail(subject=f'Personal Webpage Email from {name} ({email})', message=form.cleaned_data['message'], 
				  from_email=form.cleaned_data['email'], recipient_list=[settings.RECIPIENT_ADDRESS])
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"