import json
# features: danceability, energy, speechiness, acousticness, instrumentalness, liveness, valence

# Open songs.json and parse the song ids and song names into two separate lists
with open('songs.json') as json_data:
    d = json.load(json_data)

feature_ids = {}
tempo = []
with open('features.json') as json_data:
    f = json.load(json_data)
for feature in f['audio_features']:
    feature_ids['danceability'] = feature_ids.get('danceability',[])
    feature_ids['danceability'].append(feature['danceability']*100)
    # Store the data for the rest of the features in the same dictionary
    # All other features need to be scaled by 100
    tempo.append(feature['tempo'])

songs = {}
# Store the songs associated with their tempos in a dictionary
avgs = {}
# Calculate the averages for each feature

with open('avgs.json', 'w') as fp:
    json.dump(avgs, fp)
