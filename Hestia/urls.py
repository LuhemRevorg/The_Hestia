from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path(route='',view=index,name='index'),
    path(route='listings',view=HestListView,name='listings'),
    path(route='sublet',view=open_sublet_form,name='sublet'),
    path(route='aboutus',view=about_us,name='about'),
    path(route='signin',view=login,name='signin'),
    path(route='login_request',view=login_request,name='login_request'),
    path(route='logout',view=logout_request,name='logout'),
    path(route='dashboard',view=dashboard,name='dashboard'),
    path(route='settings',view=settings,name='settings'),
    path(route='profile',view=profile,name='profile'),
    path(route='contact',view=contact,name='contact'),
    path(route='signup',view=sign_up,name='signup'),
    path(route='sublet_request',view=sublet_request,name='sublet_request'),
    path(route='yourlistings',view=yourListings,name='yourListing'),
    path(route='cart',view=yourCart,name='Cart'),
    path(route='t&c',view=terms,name='termsconditions'),
    path(route='register',view=register_request,name='register'),
    path(route='delete',view=delete,name='account_delete'),
    path(route='remove/<int:prop_id>/',view=remove_prop,name='remove_prop'),
    path(route='remove_item/<int:item_id>/',view=remove_item,name='remove_item'),
    path(route='detail/<int:prop_id>/',view=detailView, name='detailView'),
    path(route='cart/<int:prop_id>/', view = add_to_Cart, name = 'add_to_Cart'),
    path(route='filter_listing',view=Filter,name='filter'),
]