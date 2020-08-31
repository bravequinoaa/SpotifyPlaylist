from spotifyapp import spotifyapp

songsFile = "./songs.txt" 

polkahoeURI='spotify:playlist:5jkjtIloJ4xPa4SlN2Jrp6'
quinoaURI='https://open.spotify.com/playlist/1b0IfaycrnSBdKbDvB1jmq?si=aSEeVFLkQSq8H8xjEcfYVA'
user='spotify:user:wilmondvano'


def clearFile(outputFile):
    with open(outputFile, 'w+') as f:
        f.write('')
        f.close()

def test():
    uri = songarrURI[0]
    features = s.getSongFeatures(uri, 'danceability')
    analysis = s.getSongAnalysis(uri)
    track, artist = s.getSongArtistName(uri)
    featurearr = s.getFeatureList()

    print(uri)
    print(features)
    print(f'{track} by {artist}')
    print(featurearr)
    
def getAllSongFeature():
    pass

if __name__=="__main__":
    s = spotifyapp()
    clearFile(songsFile)
    songarrURI = s.getSongURIs(polkahoeURI, songsFile)
    test()


    
    


