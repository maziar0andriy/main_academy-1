# Mapping of coutry to their domain code
countries = {
	'Ukraine': 'UA',
	'Israel': 'IL',
	'Japan': 'JP',
	'United States': 'US',
	'Sweden': 'SE'
	}

capitals = {
	'UA': 'Kiev',
	'IL': 'Jerusalem',
	'JP': 'Tokyo',
	'US': 'Washington',
	'SE': 'Stockholm'
	}
	
countries['Italy'] = 'IT'
capitals['IT'] = 'Rome'

for key, value in countries.items():
	print ("Domain for {} is {}.".format(key, value))

for key, value in capitals.items():
	print ("The capital of {} is {}".format(key, value))	

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))
		
for key, value in countries.items():
	countries[key] = [value, 'COM', 'GOV']
	
for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))