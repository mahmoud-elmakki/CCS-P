from django.shortcuts import render
from .forms import PredictForm
import numpy as np


def HomeView(request):
	return render(request, 'concrete/home.html')


def PredictView(request):

	if request.method == 'POST':
		form = PredictForm(request.POST)

		if form.is_valid():
			form = form.save()

			form.compressive_strength = prediction(form)
			compressive_strength = form.compressive_strength

			return render(request, 'concrete/result.html',
				{'compressive_strength': compressive_strength})

	else:
		form = PredictForm()

		return render(request, 'concrete/index.html', {'form': form})


def prediction(form):

		water= form.water
		wc = form.wc
		coarse_aggregate = form.coarse_aggregate
		fine_aggregate = form.fine_aggregate
		blast_furance_slag = form.blast_furance_slag
		superplasticizer = form.superplasticizer
		age = form.age

		data = [water, wc, coarse_aggregate, fine_aggregate,
			blast_furance_slag, superplasticizer, age]

		data = np.array(data)

		return final_output(data)


def final_output(data):
	return np.sum(data)