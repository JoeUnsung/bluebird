from django.db import models

class CaseList(models.Model):
    case_num = models.CharField(max_length=255)
    property_num = models.CharField(max_length=255, null=True, blank=True)
    property_type = models.CharField(max_length=255, null=True, blank=True)
    appraisal_value = models.CharField(max_length=255, null=True, blank=True)
    minimum_sale_price = models.CharField(max_length=255, null=True, blank=True)
    bidding_method = models.CharField(max_length=255, null=True, blank=True)
    sale_date = models.CharField(max_length=255, null=True, blank=True)
    property_notes = models.CharField(max_length=255, null=True, blank=True)
    location_1 = models.CharField(max_length=255, null=True, blank=True)
    location_2 = models.CharField(max_length=255, null=True, blank=True)
    location_3 = models.CharField(max_length=255, null=True, blank=True)
    responsible_person = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.case_num



# Create your models here.
