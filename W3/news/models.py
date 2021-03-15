from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify


class User(models.Model):
    username = models.CharField('نام کاربری', max_length=255, unique=True)
    password = models.CharField('پسورد', validators=[RegexValidator(
        regex='^(?=.*[A-Za-z])(?=.*[!@#$&])(?=.*\d)[A-Za-z\d!@#$&]{8,}$', message='Length has to be more than 8 character', code='nomatch')], max_length=255)
    phone = models.CharField('تلفن', max_length=200, null=True, blank=True)
    age = models.IntegerField('سن')
    image = models.ImageField(
        'عکس', upload_to="user_image/", null=True, blank=True)
    address = models.TextField('آدرس', null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super().save(*args, **kwargs)


class Author(models.Model):
    nick_name = models.CharField(max_length=255)
    rate = models.FloatField(default=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nick_name


class Category(models.Model):

    CHOICE_CAT = [
        ('Varzeshi', 'varzeshi'),
        ('Elmi', 'elmi'),
        ('Farhangi', 'farhangi'),
        ('Siasi', 'siasi'),
        ('Jenai', 'jenai'),
    ]

    REGION_CHOICE = [
        ('T', 'tehran'),
        ('E', 'esfahan'),
        ('S', 'shiraz'),
    ]
    name = models.CharField(max_length=255, choices=CHOICE_CAT, unique=True)
    region = models.CharField(max_length=255, choices=REGION_CHOICE)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    context = models.TextField()
    seen_num = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    rate = models.FloatField(default=5)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.name
