from django.db.models import Model, CharField, ForeignKey, CASCADE

# Create your models here.
class Branch(Model):
  address = CharField(max_length=255)
  name = CharField(max_length=255)

  def __str__(self):
    return self.name

ACCOUNT_TYPE_CHOICES = (('CHK', 'Checking'), ('SVG', 'Savings'), ('CRE', 'Credit'))

class Account(Model):
  branch = ForeignKey(Branch, CASCADE, related_name="account")
  owner_name = CharField(max_length=255)
  account_type = CharField(max_length=3, choices=ACCOUNT_TYPE_CHOICES)

  def __str__(self):
    return f'{self.owner_name}\'s {self.account_type} account'