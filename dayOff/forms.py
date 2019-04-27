from django import forms

from dayOff.models import DayOff
import datetime

now = str(datetime.datetime.now())[:10]


class DayOffModelForm(forms.ModelForm):
  print(">>>", now)
  if ('2019-04-11' < now):
    print('inin')
  class Meta:
    model = DayOff
    exclude = ['create_by', 'approve_status']

  def clean(self):
    cleaned_data = super().clean()
    start = str(cleaned_data.get('date_start'))
    end = str(cleaned_data.get('date_end'))

    if start < now:
      self.add_error('date_start', "Can't select past date")

    elif end < now:
      self.add_error('date_end', "Can't select past date")

    elif start > end:
      self.add_error('date_start', "Date not accurate")
      self.add_error('date_end', "Date not accurate")

    return cleaned_data
