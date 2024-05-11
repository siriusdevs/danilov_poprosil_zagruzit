from django.db import models
from datetime import datetime, timezone, date
from django.core.exceptions import ValidationError

def get_datetime_now() -> datetime:
    return datetime.now(tz=timezone.utc)

def birth_validator(date_of_birth):
    if date_of_birth > date.today():
        raise ValidationError('person date of birth cannot be in future')

class CreatedMixin(models.Model):
    created = models.DateTimeField(null=False, blank=True, default=get_datetime_now)
    class Meta:
        abstract = True

class Person(CreatedMixin):
    full_name = models.TextField(null=False, blank=False, max_length=100)
    date_of_birth = models.DateField(null=False, blank=False, validators=[birth_validator])

    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        birth_validator(self.date_of_birth)
        super().save(*args, **kwargs)

    @property
    def age(self) -> int | None:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if today.month > self.date_of_birth.month:
            return years
        if today.month == self.date_of_birth.month and today.day > self.date_of_birth.day:
            return years
        return years - 1 if years > 0 else None
    
class Equipment(CreatedMixin):
    name = models.TextField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False, max_length=500)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} of {self.person.full_name}'