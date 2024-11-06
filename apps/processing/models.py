from django.db import models

from apps.shared.models import TimeStampedModel


class UzcardHistroyRequest(TimeStampedModel):
    card_id = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    page = models.IntegerField()
    page_size = models.IntegerField()

    class Meta:
        verbose_name = "UzCardHistory"
        verbose_name_plural = "UzCardHistories"


class HumoCardHistoryRequest(TimeStampedModel):
    card_number = models.CharField(max_length=16)
    start_date = models.DateField(max_length=16)
    end_date = models.DateField(max_length=16)

    class Meta:
        verbose_name = "HumoCardHistory"
        verbose_name_plural = "HumoCardHistories"


class MasterCardHistoryRequest(TimeStampedModel):
    card_number = models.CharField(max_length=16)
    start_date = models.DateField(max_length=16)
    end_date = models.DateField(max_length=16)

    class Meta:
        verbose_name = "MasterCardHistory"
        verbose_name_plural = "MasterCardHistories"
