from django.contrib import admin
from django.urls import path

from plans.views import pension, motor_insurance, health_insurance, life_insurance, comprehesive_detail, third_party, motor_commercial, qoute

urlpatterns = [
    path('pension/', pension, name='pension'),
    path('motor_insurance/', motor_insurance, name='motor_insurance'),
    path('health_insurance/', health_insurance, name='health_insurance'),
    path('life_insurance/', life_insurance, name='life_insurance'),
    path('comprehesive_detail/', comprehesive_detail, name='comprehesive_detail'),
    path('third_party/', third_party, name='third_party'),
    path('motor_commercial/', motor_commercial, name='motor_commercial'),
    path('qoute/', qoute, name='qoute')
]
