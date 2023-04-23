from django.urls import path
from index import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('personal', views.personal_view, name='personal'),
    path('add_personal', views.add_personal_view, name='add_personal'),
    path('edit_personal', views.edit_personal_view, name='edit_personal'),
    path('delete_personal', views.delete_personal_view, name='delete_personal'),

]