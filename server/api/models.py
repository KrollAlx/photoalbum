from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField('Название альбома', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Photo(models.Model):
    title = models.CharField('Название фото', max_length=100)
    image = models.ImageField('Фото', upload_to='photos/', blank=True, default="")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)     

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

class Comment(models.Model):
    text = models.TextField('Текст комментария')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
