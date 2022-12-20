from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path("", views.PersonPageView.as_view(), name='home'),
    path("person/<slug:slug>/", views.PersonView.as_view(), name='person'),
    # path('category/<slug:slug>/', views.CategoryListView.as_view(), name='cat_list'),

    # # CRUD
    path("create/", views.CreatePersonView.as_view(), name='create'),
    path("update/<slug>", views.UpdatePersonView.as_view(), name='update'),
    # path("delete/<pk>", views.DeleteBookView.as_view(), name='delete')
]