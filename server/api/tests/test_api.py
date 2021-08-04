from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Album, Photo, Comment, Like
from api.serializers import AlbumSerializer, PhotoSerializer, CommentSerializer
from django.contrib.auth.models import User

class AuthApiTests(APITestCase):
    def setUp(self):
        self.username = 'user'
        self.password = '0000'

    def test_login(self):
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()
        url = reverse("login")        
        response = self.client.post(url, {
            "username": self.username,
            "password": self.password
        })        
        self.assertEqual(status.HTTP_200_OK, response.status_code)        

    def test_registration(self):
        url = reverse("registration")      
        response = self.client.post(url, {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)  
        self.assertIsNotNone(response.data)

class AlbumApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_authenticate(self.user)

    def test_create(self):
        url = reverse("album") 
        response = self.client.post(url, {
            "title": "new album"
        }, "json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn(Album.objects.get(title="new album"), Album.objects.all())

    def test_getMany(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        album_2 = Album.objects.create(title="album 2", user=self.user)
        url = reverse("album") 
        response = self.client.get(url)        
        serializer = AlbumSerializer([album_1, album_2], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(serializer.data, response.data)

    def test_get(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        url = reverse("album-detail", kwargs={"pk": album_1.id})  
        response = self.client.get(url)
        serializer = AlbumSerializer(album_1)
        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(serializer.data, response.data)

    def test_update(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        url = reverse("album-detail", kwargs={"pk": album_1.id})        
        response = self.client.put(url, {
            "title": "new album"
        }, "json")        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("new album", response.data["title"])

    def test_delete(self):
        album_1 = Album.objects.create(title="album 1", user=self.user)
        url = reverse("album-detail", kwargs={"pk": album_1.id})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertNotIn(album_1, Album.objects.all())

class PhotoApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_authenticate(self.user)
        self.album = Album.objects.create(title="album 1", user=self.user)
    
    def test_create(self):
        url = reverse("photo", kwargs={"album_id": self.album.id})
        response = self.client.post(url, {
            "title": "photo 1"
        }, "json")
        created_photo = Photo.objects.get(title="photo 1")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn(created_photo, Photo.objects.all())

    def test_getMany(self):
        photo_1 = Photo.objects.create(title="photo 1", album=self.album)
        photo_2 = Photo.objects.create(title="photo 2", album=self.album)
        url = reverse("photo", kwargs={"album_id": self.album.id})
        response = self.client.get(url)        
        serializer = PhotoSerializer([photo_2, photo_1], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(serializer.data, response.data)
    
    def test_get(self):
        photo_1 = Photo.objects.create(title="photo 1", album=self.album)
        url = reverse("photo-detail", kwargs={"album_id": self.album.id, "pk": photo_1.id})  
        response = self.client.get(url)
        serializer = PhotoSerializer(photo_1)
        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(serializer.data, response.data)

    def test_update(self):
        photo_1 = Photo.objects.create(title="photo 1", album=self.album)
        url = reverse("photo-detail", kwargs={"album_id": self.album.id, "pk": photo_1.id})     
        response = self.client.put(url, {
            "title": "updated title"
        }, "json")        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("updated title", response.data["title"])

    def test_delete(self):
        photo_1 = Photo.objects.create(title="photo 1", album=self.album)
        url = reverse("photo-detail", kwargs={"album_id": self.album.id, "pk": photo_1.id}) 
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertNotIn(photo_1, Photo.objects.all())

class CommentApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_authenticate(self.user)
        self.album = Album.objects.create(title="album 1", user=self.user)
        self.photo = Photo.objects.create(title="photo 1", album=self.album)
    
    def test_create(self):
        url = reverse("comments", kwargs={"photo_id": self.photo.id})
        response = self.client.post(url, {
            "text": "comment 1"
        }, "json")
        created_comment = Comment.objects.get(text="comment 1")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn(created_comment, Comment.objects.all())

    def test_getMany(self):
        comment_1 = Comment.objects.create(text="comment 1", photo=self.photo, user=self.user)
        comment_2 = Comment.objects.create(text="comment 2", photo=self.photo, user=self.user)
        url = reverse("comments", kwargs={"photo_id": self.photo.id})
        response = self.client.get(url)        
        serializer = CommentSerializer([comment_1, comment_2], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(serializer.data, response.data)

class LikeApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_authenticate(self.user)
        self.album = Album.objects.create(title="album 1", user=self.user)
        self.photo = Photo.objects.create(title="photo 1", album=self.album)

    def test_like(self):
        url = reverse("like", kwargs={"photo_id": self.photo.id})
        response = self.client.post(url)
        created_like = Like.objects.get(user=self.user, photo=self.photo)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn(created_like, Like.objects.all())

    def test_removeLike(self):
        like = Like.objects.create(user=self.user, photo=self.photo)
        url = reverse("like", kwargs={"photo_id": self.photo.id})
        response = self.client.post(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertNotIn(like, Like.objects.all())

class PopularAlbumsApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user")
        self.user.set_password("0000")
        self.user.save()
        self.client.force_authenticate(self.user)
        self.album_1 = Album.objects.create(title="album 1", user=self.user)
        self.photo_1 = Photo.objects.create(title="photo 1", album=self.album_1)
        self.photo_2 = Photo.objects.create(title="photo 2", album=self.album_1)
        Like.objects.create(user=self.user, photo=self.photo_1)
        Like.objects.create(user=self.user, photo=self.photo_2)
        self.album_2 = Album.objects.create(title="album 2", user=self.user)
        self.photo_3 = Photo.objects.create(title="photo 3", album=self.album_2)
        Like.objects.create(user=self.user, photo=self.photo_3)

    def test_popularAlbums(self):
        url = reverse("popular-albums")
        response = self.client.get(url)
        serializer = AlbumSerializer([self.album_1, self.album_2], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)