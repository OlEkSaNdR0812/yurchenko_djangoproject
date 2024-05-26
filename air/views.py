from django.shortcuts import redirect, render, get_object_or_404
from .models import SensorData
from .forms import SensorDataForm
from django.contrib.auth.decorators import login_required

@login_required
def secure_page(request):
    return render(request, 'secure.html')

def sensor_list(request):
    sensors = SensorData.objects.all()
    return render(request, 'sensor_list.html', {'sensors': sensors})

def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(SensorData, id=sensor_id)
    return render(request, 'sensor_detail.html', {'sensor': sensor})

def add_sensor(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorDataForm()
    return render(request, 'add_sensor.html', {'form': form})
