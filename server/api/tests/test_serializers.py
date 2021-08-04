from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Album, Photo, Comment, Like
from api.serializers import AlbumSerializer, PhotoSerializer, CommentSerializer, LikeSerializer

class AlbumSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_login(self.user)

    def test(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        photo_1 = Photo.objects.create(title="photo 1", album=album_1)
        photo_2 = Photo.objects.create(title="photo 2", album=album_1)
        Comment.objects.create(text="comment 1", photo=photo_1, user=self.user)
        Comment.objects.create(text="comment 2", photo=photo_2, user=self.user)
        Like.objects.create(user=self.user, photo=photo_1)
        Like.objects.create(user=self.user, photo=photo_2)

        serializer = AlbumSerializer(album_1)
        expected = {
            'id': album_1.id,
            'title': album_1.title,
            'user': self.user.id,
            'likes': 2,
            'owner': self.user.username,
            'comments': 2,
            'image': '',
            'photo_count': 2
        }
        self.assertEqual(expected, serializer.data)

class PhotoSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_login(self.user)

    def test(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        photo_1 = Photo.objects.create(title="photo 1", album=album_1)       
        comment_1 = Comment.objects.create(text="comment 1", photo=photo_1, user=self.user)
        comment_2 = Comment.objects.create(text="comment 2", photo=photo_1, user=self.user)
        Like.objects.create(user=self.user, photo=photo_1)

        serializer = PhotoSerializer(photo_1)
        expected = {
            'id': photo_1.id,
            'title': photo_1.title,
            'image': None,
            'album': album_1.id,            
            'likes': 1,
            'comments_count': 2,
            'comments': [
                {
                    'id': comment_1.id,
                    'text': comment_1.text,
                    'photo': photo_1.id,
                    'user': self.user.id,
                    'author': self.user.username
                },
                {
                    'id': comment_2.id,
                    'text': comment_2.text,
                    'photo': photo_1.id,
                    'user': self.user.id,
                    'author': self.user.username
                }
            ]
        }        
        self.assertEqual(expected, serializer.data)

class CommentSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_login(self.user)
    
    def test(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        photo_1 = Photo.objects.create(title="photo 1", album=album_1)       
        comment_1 = Comment.objects.create(text="comment 1", photo=photo_1, user=self.user)         

        serializer = CommentSerializer(comment_1)
        expected = {
            'id': comment_1.id,
            'text': comment_1.text,
            'photo': photo_1.id,
            'user': self.user.id,
            'author': self.user.username
        }        
        self.assertEqual(expected, serializer.data)

class LikeSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_login(self.user)
    
    def test(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        photo_1 = Photo.objects.create(title="photo 1", album=album_1)       
        like = Like.objects.create(user=self.user, photo=photo_1)        

        serializer = LikeSerializer(like)
        expected = {
            'id': like.id,            
            'photo': photo_1.id,
            'user': self.user.id,            
        }        
        self.assertEqual(expected, serializer.data)