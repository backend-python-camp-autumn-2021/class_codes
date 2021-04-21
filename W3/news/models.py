from django.db import models, connection
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


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
    # rate = models.FloatField(default=5)
    slug = models.SlugField(unique=True, null=True, blank=True)

    @property
    def number_of_comments(self):
        "Returns the person's full name."
        length = len(self.comment.all())
        return f'{length}'

    @property
    def abstract_context(self):
        return f'{self.context[:25]}'

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    name = models.CharField(max_length=255)
    article = models.ForeignKey(
        Article, related_name='comment', on_delete=models.CASCADE)
    comment_text = models.TextField()
    rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class PersonTehranManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(frrom='tehran')

    # TODO
    # @classmethod
    # def truncate(self):
    #     with connection.cursor() as cnc:
    #         cnc.execute(f"DELETE FROM '{cls._meta.db_table}'")


class Person(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    frrom = models.CharField(default="tehran", max_length=255)
    age = models.SmallIntegerField(null=True, blank=True)

    bachetehran = PersonTehranManager()
    objects = models.Manager()

    # @classmethod
    # def truncate(self):
    #     with connection.cursor() as cnc:
    #         cnc.execute(f"DELETE FROM '{cls._meta.db_table}'")

    class Meta:
        ordering = ['-name', '-age']
        unique_together = [['frrom', 'age']]


class A(Person):
    address = models.CharField(max_length=255)


class Personkheng(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Personkheng, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Personkheng, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Product(models.Model):
    name = models.CharField(max_length=50)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
