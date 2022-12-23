from rest_framework import serializers

from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Availability
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Timeslot
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

