from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DatesApp.models import Dates, Months
from DatesApp.serializers import DatesSerializer, MonthsSerializer
import requests

@csrf_exempt
def datesApi(request,id=0):

    xapikey = 'SECRET_API_KEY'

    if request.method=='GET':

        dates = Dates.objects.all()
        dates_serializer=DatesSerializer(dates,many=True)

        return JsonResponse(dates_serializer.data,safe=False)

    elif request.method=='POST':

        dates_data=JSONParser().parse(request)

        input_day = dates_data["Day"]

        url = "http://www.numbersapi.com/" + str(input_day) 

        response = requests.get(url)
        dates_data["Fact"] = response.text

        dates_serializer=DatesSerializer(data=dates_data)

        # validation

        if dates_serializer.is_valid():

            entered_date = dates_serializer.validated_data["Day"]
            entered_month = dates_serializer.validated_data["Month"]

            months = {
                "January": 1,
                "February": 2,
                "March": 3,
                "April": 4,
                "May": 5,
                "June": 6,
                "July": 7,
                "August": 8,
                "September": 9,
                "October": 10,
                "November": 11,
                "December": 12
            }

            if entered_date > 31 or entered_date < 1:

                return HttpResponseBadRequest("Validation error - day must be in range of 1-31")

            elif entered_month not in months.keys():

                return HttpResponseBadRequest("Validation error - enter a correct month")

            else:                
                dates_serializer.save()

                try:

                    found_month = Months.objects.get(Month=entered_month)

                    month_to_enter = MonthsSerializer(found_month,data = {"Month": entered_month, "DaysChecked": found_month.DaysChecked + 1})

                    if month_to_enter.is_valid():
                        month_to_enter.save()

                except BaseException:

                    month_to_enter = MonthsSerializer(data = {"Month": entered_month, "DaysChecked": 1})

                    if month_to_enter.is_valid():
                        month_to_enter.save()

                saved_entity = dates_serializer.data

                return JsonResponse(saved_entity,safe=False)
            

        return JsonResponse("Failed to add",safe=False)

    elif request.method=='DELETE':

        if xapikey in request.META.values():

            date=Dates.objects.get(Id=id)
            date.delete()

            return JsonResponse("Deleted successfully",safe=False)
        else:
            return HttpResponseNotAllowed()

def popularApi(request,id=0):
    if request.method=='GET':

        months = Months.objects.all()
        months_serializer=MonthsSerializer(months,many=True)

        return JsonResponse(months_serializer.data,safe=False)