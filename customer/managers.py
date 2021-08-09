from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email,  phone, password):
        if not email:
            raise ValueError('users must have email')
        if not phone:
            raise ValueError('users must have phone')
        user = self.model(email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        user = self.create_user(email, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
