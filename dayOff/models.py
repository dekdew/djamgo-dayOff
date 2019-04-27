from django.db import models


# Create your models here.
class DayOff(models.Model):
  create_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  reason = models.TextField()
  PERSONAL = '01'
  SICK = '02'
  TYPES = (
    (PERSONAL, 'Personal'),
    (SICK, 'Sick')
  )
  type = models.CharField(max_length=2, choices=TYPES, default='01')
  date_start = models.DateField()
  date_end = models.DateField()
  WAIT = '01'
  DECLINE = '02'
  APPROVE = '03'
  STATUS = (
    (WAIT, 'Wait'),
    (DECLINE, 'Decline'),
    (APPROVE, 'Approve')
  )
  approve_status = models.CharField(max_length=2, choices=STATUS, default='01')
