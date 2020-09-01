from spotifyapp import spotifyapp
from math import ceil

songsFile = "./songs.txt" 

polkahoeURI='spotify:playlist:5jkjtIloJ4xPa4SlN2Jrp6'
quinoaURI='https://open.spotify.com/playlist/1b0IfaycrnSBdKbDvB1jmq?si=aSEeVFLkQSq8H8xjEcfYVA'
user='spotify:user:wilmondvano'


def clearFile(outputFile):
    with open(outputFile, 'w+') as f:
        f.write('')
        f.close()

def t():
    arr = s.getSongDetails(songarrURI[:50])
    print(arr)

def test():
    uri = songarrURI[0]
    features = s.getSongFeatures(uri, 'danceability')
    analysis = s.getSongAnalysis(uri)
    track, artist = s.getSongArtistName(uri)

    print(uri)
    print(features)
    print(f'{track} by {artist}')
    print(featurearr)
    
def getSongNamesList(songsarr):
    # Can only send 50 tracks at a time to 
    songsArr = []
    totalsongs = len(songsarr)
    batches = ceil(totalsongs/50) 
    for i in range(batches):
        songsLeft = totalsongs - (50*i)
        if songsLeft >= 50:
            lastsong = 50*(i+1)
        else:
            lastsong = totalsongs
        sendlist = songsarr[i*50:lastsong]
        songsArr.extend(s.getSongDetails(sendlist))

    return songsArr
    

def makeFeatureArr(songs, feature):
    if feature not in features:
        return "Feature doesn't exist"
    featureArr = []
    totalsongs = len(songs)
    batches = ceil(totalsongs/100)
    for i in range(batches):
        songsLeft = totalsongs - (100*i)
        if songsLeft >= 100:
            lastsong = 100*(i+1)
        else:
            lastsong = totalsongs
        sendlist = songs[i*100:lastsong]
        featureArr.extend(s.getFeatureList(sendlist, feature))

    return featureArr
    
def filterArr(features, songsName, songsUri):
    avg = average(features)
    returnNames = []
    returnUris = []
    for i in range(len(features)):
        if features[i] >= avg:
            returnNames.append(songsName[i])
            returnUris.append(songsUri[i])
    return returnNames, returnUris 
    
def average(arr):
    return sum(arr)/len(arr)

    

if __name__=="__main__":
    s = spotifyapp()
    clearFile(songsFile)
    features = ['danceability', 'energy', 'key', 'loudness', 'mode', 
                'speechiness', 'acousticness', 'instrumentalness', 
                'liveness', 'valence', 'tempo', 'type', 'id', 
                'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']

    #songarrURI= s.getSongURIs(quinoaURI, songsFile)
    songarrURI= s.getSongURIs(polkahoeURI, songsFile)
    songsarrName = getSongNamesList(songarrURI)
    featuresarr = makeFeatureArr(songarrURI, 'danceability')
    print("average: ", average(featuresarr))
    filteredNames, filteredUris = filterArr(featuresarr, songsarrName, songarrURI)
    print(filteredNames)
    print(filteredUris)
    print("totalsongs: ", len(filteredNames))

