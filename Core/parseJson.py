import acrReco
import spotifymeta

def parseSongJson(filename,songdataJson = None):
    if songdataJson == None:
        print('ACR did not recognize the song. Skipping to next song')
    else:
        try:
            songTitle = songdataJson['metadata']['music'][0]['title']
            #youtubeLink ='https://www.youtube.com/watch?v='+songdataJson['metadata']['music'][0]['external_metadata']['youtube']['vid'])
            songArtist = songdataJson['metadata']['music'][0]['artists'][0]['name']

        except KeyError:
            print('Error Occured Anvesh debug it')
        else:
            pass
        try:
            print(songTitle)
            spotifymeta.generate_metadata(filename,songTitle)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
