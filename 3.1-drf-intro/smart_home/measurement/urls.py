from django.urls import path

from measurement.views import ListSensors, SensorView, AddSensor, UpdateSensor, AddMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('add_sensor/', AddSensor.as_view()),
    path('update_sensor/<pk>/', UpdateSensor.as_view()),
    path('add_measurement/', AddMeasurement.as_view()),
    path('all_sensors/', ListSensors.as_view()),
    path('sensor/<pk>/', SensorView.as_view())
]
