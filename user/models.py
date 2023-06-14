from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 추가 필드나 메소드 등을 정의할 수 있습니다.
    # objects = CustomUserManager()

    def __str__(self):
        return self.username