import factory
from apps.employees.enums import SENIORITY_CHOICES
from apps.employees.models import Employee, Skill


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    name = factory.Faker("word")
    years_of_experience = factory.Faker("random_int", min=0, max=10)
    seniority = factory.Iterator([choice[0] for choice in SENIORITY_CHOICES])


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    mobile_number = factory.Faker("phone_number")
    email_address = factory.Faker("email")
    street_address = factory.Faker("street_address")
    city = factory.Faker("city")
    postal_code = factory.Faker("postcode")
    country = factory.Faker("country")
    date_of_birth = factory.Faker('date_of_birth')

    @factory.post_generation
    def skills(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for skill in extracted:
                self.skills.add(skill)

