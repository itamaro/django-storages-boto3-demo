from django.db import models


class UploadedImage(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return 'UploadedImage: %s' % (self.name)
