from django.shortcuts import render
from django.views.generic import FormView

# Create your views here.
class SingUpView(FormView):
    template_name = "registration/register.html"
    form_class = SingUpForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)