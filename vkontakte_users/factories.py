from models import User
import factory
import random

class UserFactory(factory.Factory):
    FACTORY_FOR = User

    remote_id = factory.Sequence(lambda n: n)
    sex = random.choice([1,2])