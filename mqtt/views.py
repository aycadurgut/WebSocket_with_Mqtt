from django.shortcuts import render, get_object_or_404, redirect
from . import mqtt_client
from .models import Device
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeviceSerializer
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required
from rest_framework import views, status

@login_required(login_url='/account/login')
def index(request):
    
    device_list = Device.objects.all()
    parsedDeviceList = []
    for device in device_list:
        print(device.message)
        abc = str(device.message).replace('\'','')
        print("abc: ",abc) 
        myDevice = json.loads(abc)['device']
        myNewObj = {
            "id": device.id,
            "device": myDevice
        }
        parsedDeviceList.append(myNewObj)
    
    return render(request, 'index.html', {"parsedDeviceList":parsedDeviceList[::-1]})

@login_required(login_url='/account/login')
def details(request, id):
    device = get_object_or_404(Device, pk=id)
    abc = str(device.message)[:-1]
    parsed_message = json.loads(abc)
    device_data = parsed_message['device']

    if request.method == 'POST':
        print("1111")
        form = DeviceForm(request.POST, instance=device)
        print("form :",form)

        if form.is_valid():
            form.save()
            print("Form is valid. Changes saved successfully.")
            return redirect('details', id=id)
        else:
            print("Form is not valid. Errors:", form.errors)

    else:
        form = DeviceForm(instance=device, initial=device_data)

    return render(request, 'details.html', {"device_data": device_data, "form": form})

@login_required(login_url='/account/login')
def deltaTEMP(request):
    device_list = Device.objects.all()
    parsedDeviceList = []
    for device in device_list:
        print(device.message)
        abc = str(device.message)[:-1]
        print("abc: ",abc) 
        myDevice = json.loads(abc)['device']
        myNewObj = {
            "id": device.id,
            "device": myDevice
        }
        parsedDeviceList.append(myNewObj)
    return render(request, 'deltaTEMP.html', {"parsedDeviceList":parsedDeviceList})

@login_required(login_url='/account/login')
@api_view(['GET'])
def device_list(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@login_required(login_url='/account/login')
@api_view(['GET'])
def device_detail(request, id):
        device = get_object_or_404(Device, pk=id)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)