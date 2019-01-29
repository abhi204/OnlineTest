from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        full_name,
        mobile,
        email,
        college,
        department,
        sem,
        ):
        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            mobile=mobile,
            email=email,
            college=college,
            department=department,
            sem=sem,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        full_name,
        mobile,
        email,
        college,
        department,
        sem,
        password):
        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            mobile=mobile,
            email=email,
            college=college,
            department=department,
            sem=sem,
            )
        user.set_password(password)
        user.active = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100,primary_key=True)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    sem = models.IntegerField()
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    #course_id
    #score

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    USERNAME_FIELD = 'mobile'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'full_name',
        'email',
        'college',
        'department',
        'sem',
    ] 

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    def get_full_name(self):
        return self.full_name
    def email_user(self, subject, message, from_email=None):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email])
    objects = UserManager()