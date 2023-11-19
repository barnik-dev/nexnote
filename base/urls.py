from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('sign-up/', views.signup, name='signup'),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('folders/', views.folders, name='folders'),
    path('all-notes/', views.all_notes, name='all-notes'),
    path('notes/<str:pk>/', views.notes, name='notes'),
    path('edit-note/<str:pk>/', views.edit_note, name='edit-note'),
    path('delete-folder/<str:pk>/', views.delete_folder, name='delete-folder'),
    path('delete-note/<str:pk>/', views.delete_note, name='delete-note'),
    path('delete-user', views.delete_account, name='delete-user'),
    path('logout/', views.logoutUser, name='logout'),
]