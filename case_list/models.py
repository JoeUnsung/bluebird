from django.db import models

class CaseList(models.Model):
    case_id = models.AutoField(primary_key=True) ## serverless 1.0v 에서 사용
    case_num = models.CharField(max_length=255) #, primary_key=True)
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

    class Meta:
        db_table = 'case_list'  # 테이블 이름을 'case_list'로 지정
        managed = True # django가 DB를 관리 (True가 디폴트값이지만 명시적으로 작성하기)



# Create your models here.
