import factory
from django.contrib.auth.models import User
from factory import faker
from .models import Country, Address, Author, Book

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    
    title = factory.Faker("sentence", nb_works=12)
    