from dataclasses import fields
from rest_framework import serializers
from DatesApp.models import Dates, Months

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dates
        fields=('Id', 'Month', 'Day', 'Fact')

class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Months
        fields=('Id', 'Month', 'DaysChecked')