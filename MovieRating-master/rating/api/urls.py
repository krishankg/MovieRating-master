from django.urls import path

from . import views
app_name='rating'

urlpatterns=[
 path('list/',views.MovieYearAPIView.as_view(),name='list'),
 path('search/',views.MovieRatingSearchAPIView.as_view(),name='search'),
   
]