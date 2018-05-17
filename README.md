# Playlist Visualization Tutorial

![Final Product Features](https://i.imgur.com/8pNgXlc.png)
![Final Product Tempos](https://i.imgur.com/ez4Ijag.png)

### Getting Playlist Data

1. Create a Spotify account if you don't already have one and go to [Spotify's API Docs](https://beta.developer.spotify.com).

2. Open up Spotify Web Console and navigate to Playlists > Get a Playlist's Tracks

3. In your Spotify app, pick a playlist and click (...) > Share > Copy Spotify URI. Paste the URI anywhere and grab the playlist ID (`spotify:user:username:playlist:playlist_id`)

4. In the web console, fill in your `user_id` and `playlist_id` and put `items(track(name,id))` in `fields`.

5. Under `OAuth Token` click `GET TOKEN` and choose the default settings.

6. Copy paste the output and put it into a new file titled `songs.json`

7. In the [Spotify Web Console](https://beta.developer.spotify.com/console/get-audio-features-several-tracks/), navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids.

8. Copy paste the output and save it to a file titled `features.json`.

### Getting Song Features

1. Open the file titled `tinker_starter.py`.

2. Get `song_ids` and `song_names` by parsing through `songs.json`.
```
for item in d['items']:
    song_ids.append(item['track']['id'])
    song_names.append(item['track']['name'])
```

3. Edit the `song_ids` to have no quotes and spaces. You can add a line `print(*song_ids, sep=',')` after you print the IDs if you are using Python 3.

4. Parse the values for each song feature from `features.json` as follows:
```
for feature in f['audio_features']:
    feature_ids['danceability'] = feature_ids.get('danceability',[])
    feature_ids['danceability'].append(feature['danceability']*100)
```
All features, except tempo, will be scaled by 100. We will store the values for tempo separately.
5. Store all of the songs and their corresponding tempos in a dictionary.
```
songs = {}
for song in song_names:
    for t in tempo:
        songs[song] = t
```

6. Calculate the averages of each feature.
```
avgs = {}
for k,v in feature_ids.items():
    sum = 0
    for val in v:
        sum += val
    avgs[k] = sum/len(v)
```

7. The final code for this section can be viewed at `tinker.py`.

### Visualizing the data

1. Create a new file `index.html` and set up the header with a page title and import ChartJS using this link as the source: `https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js`


![Step 1](https://i.imgur.com/pTWFAYf.png)

2. In the body tags, add in the following lines:
```python
<body>
    <canvas id="songFeatures"></canvas>
    <canvas id="songTempos"></canvas>
</body>
```

3. Inside script tags, we will build our graphs. Start by creating an `averages` dictionary with the values you calculated in `tinker.py`. An example with our playlist is shown below:
```javascript
<script>
    var averages = {"danceability": 67.21851851851851, "energy": 64.74814814814815, "speechiness": 7.4185185185185185, "acousticness": 19.46912592592593, "liveness": 20.227407407407412, "valence": 49.025925925925925}
</script>
```

4. In a polarAreaChart variable, follow the structure on the [ChartJS documentation](http://www.chartjs.org/docs/latest/#creating-a-chart). This will create your first graph, showing the average feature value of songs in your selected playlist for each of the labels in the chart.
![Step 4](https://i.imgur.com/pGciqgm.png)

5. To create our tempo graph, create a variable titled barChart and set the labels to be an **array of song titles** in your playlist. Set the dataset to be the **array of tempos of the songs**.
![Step 5](https://i.imgur.com/dafFyRv.png)

6. To see your graphs on a webpage, just open `index.html` in a browser!

### Your turn to make something

Using what you've learned, Spotify's Web Console, and the ChartJS documentation, try making your own vizualizations now based on data that you're interested in!
