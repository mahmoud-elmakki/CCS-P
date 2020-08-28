from django import forms
from .models import PredictModel


class PredictForm(forms.ModelForm):

	class Meta:
		model = PredictModel
		fields = ['water', 'wc', 'coarse_aggregate', 'fine_aggregate',
				'blast_furance_slag', 'superplasticizer', 'age']

		labels = {'water': '',
				  'wc': '',
				  'coarse_aggregate': '',
				  'fine_aggregate': '',
				  'blast_furance_slag': '',
				  'superplasticizer': '',
				  'age': ''
				}

		widgets = {
			'water': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Water (kg in a m^3 mixture)'}),

			'wc': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Water/Cement Ratio'}),

			'coarse_aggregate': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Coarse Aggregate (kg in a m^3 mixture)'}),

			'fine_aggregate': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Fine Aggregate (kg in a m^3 mixture)'}),

			'blast_furance_slag': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Blast Furance Slag (kg in a m^3 mixture)'}),

			'superplasticizer': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Superplasticizer (kg in a m^3 mixture)'}),

			'age': forms.NumberInput(attrs={'class':'input-group',
											  'placeholder': 'Age (in Days)'}),
		}
