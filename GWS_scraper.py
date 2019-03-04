import requests
# from urllib2 import Request, urlopen

headers = {
  'Accept': 'application/json',
  'Authorization': 'Token 3bd65d190875cdeee907dd8eade252c665dadf5a'
}

url = 'https://api.globalwinescore.com/globalwinescores/latest/?limit=10000&offset=20000'


r = requests.get(url, headers=headers)
print(r.status_code)
print(r.headers)
print(len(r.json()['results']))

results = r.json()['results']

print("results",r.json()['results'][0])

print(type(r.json()['results']))


print(results[1])

f = open("data.csv", "a")

header_list = ['wine', 'wine_id', 'wine_slug', 'appellation', 'appellation_slug', 'color', 'wine_type', 'regions', 'country', 'classification', 'vintage', 'date', 'score', 'confidence_index', 'journalist_count']
string = '%'.join(map(str, header_list))
f.write(string)
f.write('\n')

for result in results:
        list = [result['wine'], result['wine_id'],result['wine_slug'],result['appellation'],result['appellation_slug'],result['color'],result['wine_type'],['regions'],result['country'],result['classification'],result['vintage'],result['date'],result['score'],result['confidence_index'],result['journalist_count']]
        string =  '%'.join(map(str, list))
        f.write(string)
        f.write('\n')

f.close()