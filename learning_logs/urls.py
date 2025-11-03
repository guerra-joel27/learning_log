"""defines the URL patterns for the learning_logs app"""

from django.urls import path

from . import views

app_name = "learning_logs"
urlpatterns = [
    # home page
    path("", views.index, name="index"),
    # path that shows all topics
    path("topics/", views.topics, name="topics"),
]
