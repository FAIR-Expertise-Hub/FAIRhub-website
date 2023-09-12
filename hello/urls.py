from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path('blog/<int:id>/', views.blog_page, name = "blog_page"),
    path("workshop/", views.workshop, name="workshop"),
    path("presentation/", views.presentation, name="presentation")
]
