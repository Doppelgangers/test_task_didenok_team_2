from django.db import models

from config import settings
from password.utils import EncryptionService


class PasswordStorage(models.Model):
    service_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        crypto = EncryptionService(settings.SECRET_KEY)
        self.password = crypto.encrypt(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'PasswordStorage[service_name={self.service_name}]'

    @property
    def decoded_password(self) -> str:
        crypto = EncryptionService(settings.SECRET_KEY)
        return crypto.decrypt(self.password)
