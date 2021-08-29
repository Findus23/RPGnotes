from django.urls import path

from loot import views

urlpatterns=[
    path("loot", views.LootListView.as_view(), name="lootlist"),
    path("<int:pk>/edit", views.LootEditView.as_view(), name="lootedit"),
    path("<int:pk>/delete", views.LootDeleteView.as_view(), name="lootdelete"),
    path("add", views.LootCreateView.as_view(), name="lootadd"),

]
