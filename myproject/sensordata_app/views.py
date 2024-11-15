from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import SensorData

def lista_sensordata(request):
    datos = SensorData.objects.all()  # Consulta todos los registros
    return render(request, 'sensordata_app/sensordata_list.html', {'datos': datos})


def temperature_humidity_chart(request):
    # Obtener todos los datos de la base de datos
    data = SensorData.objects.all()

    # Extraer datos de tiempo, temperatura y humedad
    times = [str(entry.datetime) for entry in data]
    temperatures = [entry.temperature for entry in data]
    humidities = [entry.humidity for entry in data]

    context = {
        'times': times,
        'temperatures': temperatures,
        'humidities': humidities,
    }

    return render(request, 'sensordata_app/chart.html', context)

