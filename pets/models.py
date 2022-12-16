from uuid import uuid4

from django.db import models


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40)
    age = models.SmallIntegerField()
    type = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Photos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pet_id = models.ForeignKey('Pet', related_name='photos', on_delete=models.CASCADE)
    url = models.ImageField(upload_to='%Y/%m/%d')

    def __str__(self) -> str:
        return str(self.id)
