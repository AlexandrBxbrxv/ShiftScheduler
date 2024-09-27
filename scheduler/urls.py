from django.urls import path

from scheduler.apps import SchedulerConfig
from scheduler.views import HomePage

app_name = SchedulerConfig.name

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
]
