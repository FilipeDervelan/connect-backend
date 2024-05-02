from django.db import models

class Ministry(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255, null=True, blank=True)
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
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "function"
        verbose_name_plural = "Functions"

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    birth_day = models.DateField(null=True, blank=True)
    email = models.EmailField()
    function = models.ManyToManyField(Function, null=True, blank=True)
    ministry = models.ManyToManyField(Ministry, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

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
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return f"{self.name} ' - ' {self.description}"

class Scale(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    song = models.ManyToManyField(Song, null=True, blank=True)
    participant = models.ManyToManyField(User, null=True, blank=True)
    function = models.ManyToManyField(Function, null=True, blank=True)
    ministry = models.ForeignKey(Ministry, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "scale"
        verbose_name_plural = "Scales"

    def __str__(self):
        return self.name

class Unavailability(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "unavailability"
        verbose_name_plural = "Unavailabilities"

    def __str__(self) -> str:
        return f"{self.user.name} ' - ' {self.start_date} ' - ' {self.end_date}"