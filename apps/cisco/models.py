from django.db.models.functions import TruncDate
from django.db import models

from apps.shared.models import TimeStampedModel


class ResourceStats(TimeStampedModel):
    resourceId = models.CharField(max_length=56)
    resourceName = models.CharField(max_length=128)
    timeChangedStateMillis = models.BigIntegerField()
    nHandledContacts = models.IntegerField()
    nPresentedContacts = models.IntegerField()
    avgTalkDuration = models.BigIntegerField()
    longestTalkDuration = models.BigIntegerField()
    avgHoldDuration = models.BigIntegerField()
    longestHoldDuration = models.BigIntegerField()
    avgWorkDuration = models.BigIntegerField()
    totalTalkTime = models.BigIntegerField()
    totalHoldTime = models.BigIntegerField()
    maxReadyTime = models.BigIntegerField()
    avgReadyTime = models.BigIntegerField()
    totalReadyTime = models.BigIntegerField()
    maxNotReadyTime = models.BigIntegerField()
    avgNotReadyTime = models.BigIntegerField()
    totalNotReadyTime = models.BigIntegerField()
    maxWorkTime = models.BigIntegerField()
    totalWorkTime = models.BigIntegerField()
    logonDuration = models.BigIntegerField()
    avgSpeedOfAnswer = models.IntegerField()
    rsrcCurrentStateReason = models.CharField(max_length=128, null=True, blank=True)
    activeOutboundTalkDuration = models.BigIntegerField()
    avgOutboundTalkDuration = models.BigIntegerField()
    avgOutboundHoldDuration = models.BigIntegerField()
    activeOutboundHoldDuration = models.BigIntegerField()
    longestOutboundTalkDuration = models.BigIntegerField()
    longestOutboundHoldDuration = models.BigIntegerField()
    totalOutboundTalkTime = models.BigIntegerField()
    totalOutboundHoldTime = models.BigIntegerField()
    avgOutboundWorkTime = models.BigIntegerField()
    maxOutboundWorkTime = models.BigIntegerField()
    totalOutboundWorkTime = models.BigIntegerField()
    avgOutboundTalkWindow1 = models.BigIntegerField()
    avgOutboundHoldWindow1 = models.BigIntegerField()
    avgOutboundTalkWindow2 = models.BigIntegerField()
    avgOutboundHoldWindow2 = models.BigIntegerField()
    avgTalkingWindow1 = models.BigIntegerField()
    avgHoldWindow1 = models.BigIntegerField()
    avgTalkingWindow2 = models.BigIntegerField()
    avgHoldWindow2 = models.BigIntegerField()
    strResourceState = models.CharField(max_length=128, null=True, blank=True)
    resourceBusySubState = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.resourceName

    class Meta:
        constraints = [
            models.UniqueConstraint(TruncDate("created_at"), "resourceId", name="date_unique"),
        ]
