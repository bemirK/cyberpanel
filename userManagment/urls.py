from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadUserHome, name='loadUsersHome'),
    path('viewProfile/', views.viewProfile, name='viewProfile'),
    path('createUser/', views.createUser, name='createUser'),
    path('submitUserCreation/', views.submitUserCreation, name='submitUserCreation'),
    path('modifyUsers/', views.modifyUsers, name='modifyUsers'),
    path('fetchUserDetails/', views.fetchUserDetails, name='fetchUserDetails'),
    path('saveModifications/', views.saveModifications, name='saveModifications'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    path('submitUserDeletion/', views.submitUserDeletion, name='submitUserDeletion'),
    path('createNewACL/', views.createNewACL, name='createNewACL'),
    path('createACLFunc/', views.createACLFunc, name='createACLFunc'),
    path('deleteACL/', views.deleteACL, name='deleteACL'),
    path('deleteACLFunc/', views.deleteACLFunc, name='deleteACLFunc'),
    path('modifyACL/', views.modifyACL, name='modifyACL'),
    path('fetchACLDetails/', views.fetchACLDetails, name='fetchACLDetails'),
    path('submitACLModifications/', views.submitACLModifications, name='submitACLModifications'),
    path('changeUserACL/', views.changeUserACL, name='changeUserACL'),
    path('changeACLFunc/', views.changeACLFunc, name='changeACLFunc'),
    path('resellerCenter/', views.resellerCenter, name='resellerCenter'),
    path('saveResellerChanges/', views.saveResellerChanges, name='saveResellerChanges'),
    path('apiAccess/', views.apiAccess, name='apiAccess'),
    path('saveChangesAPIAccess/', views.saveChangesAPIAccess, name='saveChangesAPIAccess'),
    path('listUsers/', views.listUsers, name='listUsers'),
    path('fetchTableUsers/', views.fetchTableUsers, name='fetchTableUsers'),
    path('controlUserState/', views.controlUserState, name='controlUserState'),
]
