from django.urls import path
# Import view
from .views import HomePageView, world_dataset, kecities_datasets

# Define a pattern 
urlpatterns = [
    # When a the page loads, automatically load the html file.  
    path('', HomePageView.as_view(), name='home'),
    # path('about/', views.about, name='about'),

    # Datasets to be serialized , request, view name, and , name to be used inside
    # the html script as reference to data passed to map
    path('kenyan_cities/', kecities_datasets, name='ke_cities'),
    path('world_countries/', world_dataset, name='wld_countries'),
]