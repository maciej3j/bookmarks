from django.conf import settings
from django.db.models import CASCADE, DateField, ImageField, Model, OneToOneField


class Profile(Model):
    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date_of_birth = DateField(blank=True, null=True)
    photo = ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
