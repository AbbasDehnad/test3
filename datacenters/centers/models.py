from django.db import models

# Create your models here.


class CentersModel(models.Model):
    interface_name = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    vlan_id = models.IntegerField(blank=True, null=True)
    ipv6_address = models.CharField(max_length=100,   blank=True, null=True)
    prefix_length = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.interface_name} {self.vlan_id} {self.created_at} "
