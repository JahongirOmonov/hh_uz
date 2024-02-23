from django.db import models
from utils.models import BaseModel
from users.models import User
from utils.choices import Type, TypeOfWork, WorkingTime


class Region(BaseModel):
    title = models.CharField(max_length=31)
    neighbour = models.ManyToManyField('self', related_name='children', blank=True, null=True)

    def __str__(self):
        return self.title

class District(BaseModel):
    title = models.CharField(max_length=31)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.title


class Company(BaseModel):
    title = models.CharField(max_length=31)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Experience(BaseModel):
    title = models.CharField(max_length=31, choices=Type.choices, default=Type.INEXPERIENCED)


    def __str__(self):
        return self.title


class Job(BaseModel):
    typeOfWork = models.CharField(max_length=7, choices=TypeOfWork.choices, default=TypeOfWork.OF)
    workingTime = models.CharField(max_length=10, choices=WorkingTime.choices, default=WorkingTime.FULL)
    title = models.CharField(max_length=31)
    description = models.CharField(max_length=127, blank=True, null=True)


    price_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    career = models.CharField(max_length=31, blank=True, null=True)

    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="jobs")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    profession_type = models.ForeignKey('ProfessionType', on_delete=models.CASCADE, related_name="jobs")

    def __str__(self):
        return self.title

class Profession(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title

class ProfessionType(BaseModel):
    title = models.CharField(max_length=31)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='profession_types')


    def __str__(self):
        return f"{self.title} --> {self.profession}"

class like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} -- > {self.job}"


class unshow(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job} -- > {self.user}"








