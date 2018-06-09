from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import WeightEntry
from django.db.models.functions import Trunc
from django.db.models import DateField
from datetime import datetime
from django.urls import reverse
from math import fabs
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

	return render(request, 'weight_tracker/view_data.html', {'weight_data' : weight_data, 'avg_min' : total_min_weight, 'avg_max' : total_max_weight, 'avg_var' : total_variance})

def add_entry(request):
	if request.method == "POST":
		date = str(request.POST['date'])
		min_weight = int(request.POST['min'])
		max_weight = int(request.POST['max'])

		if min_weight > max_weight:
			return HttpResponse("min weight must be lesser or equal to the max weight!")

		new_weight_entry = WeightEntry(min_weight=min_weight, max_weight=max_weight, variance=fabs(max_weight - min_weight))
		new_weight_entry.save()

		new_weight_entry.data_date = datetime.strptime(date, '%Y-%m-%d')
		new_weight_entry.save()

		return HttpResponseRedirect(reverse('detail', args = {new_weight_entry.id}))
	else:
		return render(request, 'weight_tracker/add_data.html')

def view_data_detail(request, entry_id):
	weight_entry = get_object_or_404(WeightEntry, pk=entry_id)
	return render(request, 'weight_tracker/detail.html', {'data' : weight_entry})
