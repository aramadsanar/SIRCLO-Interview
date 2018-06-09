from django.test import TestCase
from .models import WeightEntry
from math import fabs
from datetime import datetime
# Create your tests here.
class WeightTrackerTest(TestCase):
	def test_variance_test(self):
		min_weight = 10
		max_weight = 8
		variance_test = WeightEntry(min_weight=min_weight, max_weight=max_weight, variance=fabs(min_weight - max_weight))
		self.assertEquals(variance_test.variance, 2)


	def test_date_entry_test(self):
		date_test = WeightEntry(min_weight=1, max_weight=2, variance=1)
		date_test.save()
		date_test.data_date = datetime.strptime('2009-12-12', '%Y-%m-%d')
		date_test.save()

		expected_date = '2009-12-12'
		extracted_date = date_test.data_date.strftime('%Y-%m-%d')

		date_test.delete();

		self.assertEquals(expected_date, extracted_date)

