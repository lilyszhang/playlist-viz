import json

song_ids = []
with open('songs.json') as json_data:
    d = json.load(json_data)
    for item in d['items']:
        song_ids.append(item['track']['id'])

print(song_ids)
