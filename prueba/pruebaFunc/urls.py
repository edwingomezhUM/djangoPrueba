from django.urls import path
from pruebaFunc import views

urlpatterns = [
    # path('getTracks/', views.prueba_list, name='tracks_get'),
    path('insertTracks/', views.insertTracks, name='insert_track'),
    path('delTracks/', views.delTracks, name='del_track'),
    path('getTopTracks/', views.topTracks, name='top_tracks'),
    path('getTracksName/', views.tracksName, name='tracksName'),
    path('insertData/', views.insertData, name='insertData'),
    
]