from django.db import models
from django.utils.crypto import get_random_string

import random
import string


# Create your models here.
def random_string():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return get_random_string(14, chars)


class VerificationCode(models.Model):
    code = models.CharField(max_length=14, default=random_string)
    validity = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
