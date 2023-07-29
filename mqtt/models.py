from django.db import models

class Device(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255,default="placeholder",null=True)
    message = models.TextField(default="",null=True)
    device_serial = models.CharField(max_length=10240,default="placeholder",null=True)

    def __str__(self):
        return self.topic
