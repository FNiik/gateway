from django.db import models

# Create your models here.
class Gateway(models.Model):
    name= models.CharField(max_length=100, unique=True)
    ip_address= models.GenericIPAddressField(unique=True)
    port_number= models.PositiveIntegerField()
    description= models.TextField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    io = models.CharField(max_length=10, choices=[('input', 'Input'), ('output', 'Output')],null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')],null=True, blank=True , default='active')
    location = models.CharField(blank=True, null=True, max_length=50)
    def __str__(self):
        return f"{self.name} ({self.ip_address}:{self.port_number})"
    
