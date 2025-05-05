from django.db import models
from django.contrib.auth.models import AbstractUser


class Ministry(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255, null=True, blank=True)
    owner_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "ministry"
        verbose_name_plural = "Ministries"

    def __str__(self):
        return self.name


class Function(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ministry = models.ForeignKey(
        Ministry, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "function"
        verbose_name_plural = "Functions"

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    birth_day = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    function = models.ManyToManyField(Function, blank=True)
    ministry = models.ManyToManyField(Ministry, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "custom_user"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.get_full_name() or self.username


class Singer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "singer"
        verbose_name_plural = "Singers"

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    singer = models.ForeignKey(
        Singer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return f"{self.name} {f'- {self.singer.name}' if self.singer else ''}"


class Scale(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    song = models.ManyToManyField(Song, null=True, blank=True)
    participant = models.ManyToManyField(CustomUser, null=True, blank=True)
    ministry = models.ForeignKey(Ministry, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "scale"
        verbose_name_plural = "Scales"

    def __str__(self):
        return f"{self.name} - {self.date} - {self.ministry.name}"


class Unavailability(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "unavailability"
        verbose_name_plural = "Unavailabilities"

    def __str__(self) -> str:
        return f"{self.user.username} - {self.start_date} - {self.end_date}"
