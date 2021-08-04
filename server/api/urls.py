from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('album', views.AlbumList.as_view(), name="album"),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name="album-detail"),
    path('popular-albums', views.PopularAlbums.as_view(), name="popular-albums"),

    path('<int:album_id>/photo', views.PhotoList.as_view(), name="photo"),
    path('<int:album_id>/photo/<int:pk>', views.PhotoDetail.as_view(), name="photo-detail"),
    
    path('<int:photo_id>/comments', views.CommentList.as_view(), name="comments"),
    path('<int:photo_id>/like', views.LikeCreate.as_view(), name="like"),

    path('auth/login', obtain_auth_token, name="login"),
    path('auth/registration', views.RegisterView.as_view(), name="registration"),
] 
