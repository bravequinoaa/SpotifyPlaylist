import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class spotifyapp:
    def __init__(self):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

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
        # TODO:
        # set up someone only the desired feature is returned
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
        result = self.spotify.track(uri)
        songname = result['name']
        artistname = (result['artists'])[0]['name']
        return songname, artistname
    
    def getFeatureList(self):
        uri = 'spotify:track:5PJKbLCiIkQgir60Sd8DQ5'
        result = self.spotify.audio_features(uri)[0]
        features = []
        for key in result:
            features.append(key)

        return features 

