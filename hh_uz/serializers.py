from rest_framework import serializers
from .models import Company, Experience, ProfessionType, Job, Region


# class ExperienceSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(source='get_title_display')
#     class Meta:
#         model = Experience
#         fields = (
#             "id",
#             "title"
#         )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "title",
            "is_verified",
            "image",
            "created_at"
        )

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title')


class JobSerializer(serializers.ModelSerializer):
    typeOfWork = serializers.CharField(source='get_typeOfWork_display')
    experience = serializers.StringRelatedField(source="experience.title")
    region = serializers.StringRelatedField(source="region.title")
    company = serializers.StringRelatedField(source="company.title")
    profession_type = serializers.StringRelatedField(source="profession_type.title")
    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "description",
            "typeOfWork",
            "price_from",
            "price_to",
            "career",
            "experience",
            "region",
            "company",
            "profession_type",
            "created_at"
        )

class CustomJobSerializer(serializers.ModelSerializer):
    profession_type = serializers.StringRelatedField(source="profession_type.title")
    region = serializers.StringRelatedField(source="region.title")
    company = serializers.StringRelatedField(source="company.title")
    class Meta:
        model = Job
        fields = (
            "profession_type",
            "price_from",
            "price_to",
            "region",
            "company"
        )

class JobDetailSerializer(serializers.ModelSerializer):
    experience = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = (
            "title",
            "experience",
            "description",
            "workingTime"

        )

class SimilarJobSerializer(serializers.ModelSerializer):
    profession_type = serializers.StringRelatedField(source="profession_type.title")
    region = serializers.StringRelatedField(source="region.title")
    company = serializers.StringRelatedField(source="company.title")
    class Meta:
        model = Job
        fields = (
            "title",
            "profession_type",
            "price_from",
            "price_to",
            "region",
            "company"
        )








class ProfessionTypeSerializer(serializers.ModelSerializer):
    job_count = serializers.IntegerField()

    class Meta:
        model = ProfessionType
        fields = ('id', 'title', 'job_count')


class JobListSerializer(serializers.ModelSerializer):
    typeOfWork = serializers.CharField(source='get_typeOfWork_display')
    experience = serializers.StringRelatedField(source="experience.title")
    region = serializers.StringRelatedField(source="region.title")
    company = serializers.StringRelatedField(source="company.title")
    image = serializers.StringRelatedField(source="company.image")
    profession_type = serializers.StringRelatedField(source="profession_type.title")
    class Meta:
        model = Job
        fields = (
            "title",
            "typeOfWork",
            "price_from",
            "price_to",
            "experience",
            "region",
            "company",
            "profession_type",
            "created_at",
            "image"
        )





