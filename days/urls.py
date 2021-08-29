from django.urls import path

from days import views

urlpatterns=[
    path("", views.list_day_redirect, name="daylist"),
    path("add", views.DayCreateView.as_view(), name="dayadd"),
    path("<int:day>", views.DayDetailView.as_view(), name="daydetail"),
    path("<int:day>/edit", views.DayEditView.as_view(), name="dayedit"),
    path("<int:day>/delete", views.DayDeleteView.as_view(), name="daydelete"),

]
