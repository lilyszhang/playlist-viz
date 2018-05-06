![Final Product](https://i.imgur.com/8pNgXlc.png)

# Playlist Visualization Tutorial

### Getting Playlist Data

1. Create a Spotify account if you don't already have one and go to [Spotify's API Docs](beta.developer.spotify.com).

2. Open up Spotify Web Console and navigate to Playlists > Get a Playlist's Tracks

3. In your Spotify app, pick a playlist and click (...) > Share > Copy Spotify URI. Paste the URI anywhere and grab the playlist ID (`spotify:user:username:playlist:playlist_id`)

4. In the web console, fill in your `user_id` and `playlist_id` and put `items(track(album(name,href),id))` in `fields`.

5. Under `OAuth Token` click `GET TOKEN` and choose the default settings.

6. Copy paste the output and put it into a new file titled `songs.json`

### Getting Song Features

1. Get `song_ids` and `song_names` by parsing through `songs.json`

2. Edit the `song_ids` to have no quotes and spaces.

3. In the Spotify Web Console, navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids.

4. Copy paste the output and save it to a file titled `features.json`
