from django.db.models import Model, CharField

# Create your models here.
class Branch(Model):
  address = CharField(max_length=255)
  name = CharField(max_length=255)
