from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import LoginForm


# Create your views here.
# loginView - LogoutView
class loginView(FormView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("success")


def form_valid(self, form):
    username = form.data.get("username", None)
    password = form.dara.get("password", None)

    if username == "username" and password == "admin":

        self.request.session.flush()
        self.request.session["user_id"] = username

    return HttpResponseRedirect(self.success_url)


def form_valid(self, form):
    username = form.data.get("username", None)
    password = form.dara.get("password", None)

    if username == "username" and password == "admin":
        self.request.session.flush()
        self.request.session["user_id"] = username

        return HttpResponseRedirect(self.success_url)
    else:
        return super().form_valid(self.request)
