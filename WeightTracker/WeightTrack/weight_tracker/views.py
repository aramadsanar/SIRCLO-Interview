from django.shortcuts import render
from django.http import HttpResponse
from .models import WeightEntry
from django.db.models.functions import Trunc
from django.db.models import DateField
# Create your views here.
def view_entries(request):
	weight_data = WeightEntry.objects.order_by(Trunc('data_date', 'date', output_field=DateField()).desc())
	total_min_weight = 0
	total_max_weight = 0
	total_variance = 0
	data_count = 0
	if weight_data:
		for wd in weight_data:
			total_min_weight += wd.min_weight
			total_max_weight += wd.max_weight
			total_variance += wd.variance
			data_count += 1

		total_max_weight /= data_count
		total_min_weight /= data_count
		total_variance /= data_count

	return render(request, 'view_data.html', {'weight_data' : weight_data, 'avg_min' : total_min_weight, 'avg_max' : total_max_weight, 'avg_var' : total_variance})

def add_entry(request):
	return HttpResponse("You are on add entry page")

def view_data_detail(request, date):
	return HttpResponse("You are seeing the detail for %s" % str(date))
