import inspect
from enum import Enum

__author__ = 'Ashraful'


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not (m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(p[1].value, p[0]) for p in props])
        return choices


class GenderEnum(ChoiceEnum):
    MALE = 'Male'
    FEMALE = "Female"
    OTHER = "Other"
