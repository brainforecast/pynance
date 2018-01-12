#goog_pynance
#No License. www.brainforecast.com
import json, requests, sys
file_names = ['TSX', 'TSXV']
goog_names = ['TSE', 'CVE']

for i in range(0, len(file_names)):
	fread = open(file_names[i] + '.txt')
	fwrite = open(file_names[i] + '_output.txt', 'w')
	#print(fread.readlines())
	for line in fread.readlines():
		ticker_symbol = line.split("\t")[0]
		print(ticker_symbol)
		try:
			url = 'https://finance.google.com/finance?q={}:{}&output=json'.format(goog_names[i], ticker_symbol)
			print(url)
			response = requests.get(url)
			response.raise_for_status()
			response.text
			fin_data = json.loads(response.content[6:-2].decode('unicode_escape'))
			print_data = json.dumps(fin_data)
			fwrite.write(print_data)
			print("!")
		except:
			print("X")
			continue

	#url = 'https://finance.google.com/finance?q=TSE:NXE&output=json'
	#response = requests.get(url)
	#response.raise_for_status()
	#print(response.text)