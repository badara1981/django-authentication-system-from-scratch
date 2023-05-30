from django.urls import path


urlpatterns = [
path("login/",loginView.as_view(), name="login"),

]
