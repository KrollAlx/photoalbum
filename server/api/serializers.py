from django.db.models import fields
from .models import Album
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_superuser')
    
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AlbumSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    photo_count = serializers.SerializerMethodField()

    def get_likes(self, instance):       
        return sum(photo.like_set.count() for photo in instance.photo_set.all())
    
    def get_owner(self, instance):
        return instance.user.username
    
    def get_comments(self, instance):        
        return sum(photo.comment_set.count() for photo in instance.photo_set.all())

    def get_photo_count(self, instance):
        return instance.photo_set.count()

    def get_image(self, instance):
        photos = instance.photo_set.all()
        if len(photos) != 0 and photos[0].image:
            return "http://localhost:8000" + photos[0].image.url if photos[0].image.url != "" else ""
        else:
            return ""

    class Meta:
        model = Album
        fields = ('id', 'title', 'user', 'likes', 'owner', 'comments', 'image', 'photo_count')

class PhotoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_likes(self, instance):
        return instance.like_set.count()

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comment_set.all(), many=True)
        return serializer.data

    def get_comments_count(self, instance):        
        return instance.comment_set.count()

    class Meta:
        model = Photo
        fields = ('id', 'title', 'image', 'album', 'likes', 'comments_count', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, instance):
        return instance.user.username

    class Meta:
        model = Comment
        fields = ('id', 'text', 'photo', 'user', 'author')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'