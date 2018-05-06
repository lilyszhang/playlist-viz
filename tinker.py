import json

song_ids = []
song_names = []
with open('songs.json') as json_data:
    d = json.load(json_data)
    for item in d['items']:
        song_ids.append(item['track']['id'])
        song_names.append(item['track']['name'])

print('Song IDs: ' + str(song_ids) + '\n')

feature_ids = {}
tempo = []
with open('features.json') as json_data:
    f = json.load(json_data)
features = ['danceability','energy','speechiness','acousticness','liveness','valence']
for song in f['audio_features']:
    for feature in features:
        feature_ids[feature] = feature_ids.get(feature,[])
        feature_ids[feature].append(song[feature]*100)
    tempo.append(song['tempo'])

songs = {}
for song in song_names:
    for t in tempo:
        songs[song] = t
avgs = {}

for k,v in feature_ids.items():
    sum = 0
    for val in v:
        sum += val
    avgs[k] = sum/len(v)

print('Song Titles: ' + str(songs.keys()) + '\n')
print('Feature Averages: ' + str(avgs) + '\n')

with open('avgs.json', 'w') as fp:
    json.dump(avgs, fp)
