import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


class spotifyapp:
    def __init__(self):
        self.scope = 'playlist-modify-private'
        self.client_id = '77fde354c3c94b0d842c2f5d387b1c7d'
        self.client_secret = 'cef8ee0d11154423913dbe3f1020ba1b'
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                                 client_secret=self.client_secret,
                                                                 scope=self.scope, 
																 redirect_uri='localhost:8888/callback',
                                                                 cache_path='./'))

    def getSongURIs(self, playlist, outputFile):
        totalSongs = 0 
        songarr = []
        iteration = 0 

        while totalSongs % 100 == 0:
            iteration+=1 
            result = self.spotify.playlist_tracks(playlist_id=playlist, offset=totalSongs)
            resultLength = len(result['items'])
            totalSongs += resultLength
                
            resultSongs = []

            for i in range(resultLength):
                songURI = ((((result['items'])[i])['track'])['uri'])
                resultSongs.append(songURI)
                songarr.append(songURI)

            with open(outputFile, 'a+') as f:
                for song in resultSongs:
                    f.write(song + '\n')

            if resultLength != 100:
                break

        print(iteration)
        return songarr

    def getSongFeatures(self, uri, feature=None):
        # can pass entire songarr
        result = self.spotify.audio_features(uri)[0]

        if feature == None:
            return result
        try:
            featureVal = result[str(feature)]
        except e:
            return "Feature not found"
        return f'{feature}: {featureVal}'

    def getSongAnalysis(self, uri):
        # this is probably too deep than what I actually ened
        # might be useful if i do the genre ML problem
        result = self.spotify.audio_analysis(uri)
        return result

    def getSongArtistName(self, uri):
        # Can pass 50 at a time wihth spotify.tracks()h
        result = self.spotify.track(uri)
        songname = result['name']
        artistname = (result['artists'])[0]['name']
        return songname, artistname
    
    def getFeatureList(self, uris, feature = None):
        # can pass 100 uris
        # we trust feature is valid 
        features = []
        for uri in uris:
            if feature:
                result = (self.spotify.audio_features(uri)[0])[feature]
            else:
                result = self.spotify.audio_features(uri)[0]

            features.append(result)

        return features 
    
    def getSongDetails(self, uris):
        # [ [songname, artist], ]
        songdetails = []
        result = self.spotify.tracks(uris)['tracks']
        for i in range(len(uris)):
            songname = (result[i])['name']     
            artistname = (((result[i])['artists'])[0])['name']
            songdetails.append( (songname, artistname) )
        return songdetails

    def fillPlaylist(self, songURIs, playlistURI):
        self.spotify.playlist_add_items(playlistURI, songURIs)
        
    







