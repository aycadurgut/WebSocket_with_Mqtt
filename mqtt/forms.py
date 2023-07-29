from django import forms
from .models import Device
from django.forms import widgets

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        labels = {
            'topic': "Topic",
            'message': "Message",
            'device_serial': "Device Serial",
        }
        widgets = {
            "topic": widgets.TextInput(attrs={'class': 'form-control'}),
            "message": widgets.Textarea(attrs={'class': 'form-control'}),
            "device_serial": widgets.NumberInput(attrs={'class': 'form-control'}),
        }