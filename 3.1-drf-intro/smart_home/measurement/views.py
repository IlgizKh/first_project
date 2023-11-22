# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


# 1. Создать датчик. Указываются название и описание датчика.
class AddSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
# 2. Изменить датчик. Указываются название и описание.
class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# 3. Добавить измерение. Указываются ID датчика и температура.
class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# 4 Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class ListSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# 5 Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer