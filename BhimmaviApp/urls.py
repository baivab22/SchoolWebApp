from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homeview.as_view(), name='home'),  # Example view mapping
    path('home', views.Homeview.as_view(), name='home'),
    path('event/<int:pk>', views.event_detail, name='event'),
    path('event', views.event_list, name='event'),
    path('blogpost/<int:pk>/', views.blogpost_detail, name='blogpost_detail'),

    path('blogpost',views.blogpost_list, name='blogpost'),
    path('alumni/<int:pk>',views.alumni_detail, name='alumni'),
    path('alumni',views.alumni_list, name='alumni'),
    path('gallery/', views.gallery_category, name='gallery'),
    path('gallery/<str:gallery_title>/<str:category>', views.gallery_list, name='gallery'),
    path('testimonials/', views.testimonial_view, name='testimonial'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', views.contact_view, name='contact'),
    path('enquiry/', views.enquiry_view, name='enquiry'),
    path('teachers/', views.teachers, name='teachers'),
    path('bod_members/', views.bod_member, name='bod_member'),
    path('bod_details/<int:pk>/', views.bod_details, name='bod_member'),
    path('admission', views.admission_view, name='admission'),
    path('introduction', views.introduction, name='introduction'),
    path('history', views.history, name='history'),


]

