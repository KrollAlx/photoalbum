from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AlbumSerializer, CommentSerializer, LikeSerializer, PhotoSerializer, UserSerializer
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated

class AlbumList(generics.ListCreateAPIView):   
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user.pk)        
    
    def create(self, request, *args, **kwargs):       
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return Album.objects.filter(user=self.request.user.pk)

    def update(self, request, *args, **kwargs):       
        request.data['user'] = request.user.pk
        return super().update(request, *args, **kwargs)

class PopularAlbums(APIView):    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        popular_albums = sorted(serializer.data, key=lambda album: album['likes'], reverse=True)
        return Response(data=popular_albums)
    

class PhotoList(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        album_id = self.kwargs['album_id']       
        return Photo.objects.filter(album=album_id)

    def create(self, request, *args, **kwargs):
        request.data['album'] = self.kwargs['album_id']
        return super().create(request, *args, **kwargs)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Photo.objects.filter(album=album_id)   

    def update(self, request, *args, **kwargs):
        request.data['album'] = self.kwargs['album_id']
        return super().update(request, *args, **kwargs)

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        photo_id = self.kwargs['photo_id']
        return Comment.objects.filter(photo=photo_id)

    def create(self, request, *args, **kwargs):
        request.data['photo'] = self.kwargs['photo_id']
        request.data['user'] = self.request.user.pk
        return super().create(request, *args, **kwargs)

class LikeCreate(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        '''Если на данном фото уже стоит лайк от заданного пользователя, то лайк удаляется'''
        try:
            photo_id = self.kwargs['photo_id']
            like = Like.objects.get(photo_id=photo_id,user_id=request.user.pk)
            like.delete()
            response_data = self.get_serializer(instance=like).data
            return Response(data=response_data)
        except:
            request.data['user'] = self.request.user.pk
            request.data['photo'] = photo_id
            return super().create(request, *args, **kwargs)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer