from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50, unique=True)

  def __str__ (self):
      return self.name


class Post(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=140,
                              blank=True, null=True)
  slug = models.SlugField(max_length=50, unique=True)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  blog = models.ForeignKey(Blog)
  author = models.ForeignKey(settings.AUTH_USER_MODEL)

  class Meta:
    ordering = ['-created']

  def __str__ (self):
      return self.title

class Poll(models.Model):
    question = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug

class Choice(models.Model):
    poll = models.ForeignKey(Poll)

    PEPPERONI = 'pepperoni'
    MUSHROOMS = 'mushrooms'
    ONIONS = 'onions'
    SUASAGE = 'sausage'
    OLIVES = 'olives'
    PEPPERS = 'bell peppers'
    CHEESE = 'cheese'
    BEST_TOPPING = (
        (PEPPERONI, 'pepperoni'),
        (MUSHROOMS, 'mushrooms'),
        (ONIONS, 'onions'),
        (SUASAGE, 'sausage'),
        (OLIVES, 'olives'),
        (PEPPERS, 'bell peppers'),
        (CHEESE, 'cheese'),
    )
    answer = models.CharField(
        max_length = 50,
        choices = BEST_TOPPING,
        default = CHEESE,
    )
    votes = models.IntegerField(default=0)
