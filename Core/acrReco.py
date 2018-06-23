#Install acrcloud_sdk_python
# python -m pip install git+https://github.com/acrcloud/acrcloud_sdk_python

#Audio fingerprinting and metadata fetch from ACR Cloud
#Create a developer account at acrcloud https://ap-console.acrcloud.com/service/avr
#In dashboard select Audio Video Recognization
#Create Project
#Name the Project
#Select Recorded Audio in Audio Source
#Select ACR Cloud Music in Buckets
#Enable 3rd Party Integration and click on Create

#Enter Host, Access key, Access Secret

import os, sys,json
from acrcloud.recognizer import ACRCloudRecognizer

if __name__ == '__main__':
    config = {
        #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
        'host':'identify-ap-southeast-1.acrcloud.com',
        'access_key':'fbb16757f6ea852d81de6f0a064a8d2f',
        'access_secret':'arSiG2EtvkeRqzAwEOuKPkYLQr4PLXwz9nYXW48w',
        'timeout':10 # seconds
    }

    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    #print (re.recognize_by_file(sys.argv[1], 0))

    buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    songdata = re.recognize_by_filebuffer(buf, 0)

    #converting string data to Json
    songdataJson = json.loads(songdata)

    print(songdataJson)
    print('\n','Title:-> '+songdataJson['metadata']['music'][0]['title'])
    print('\n','Youtube link:-> '+ 'https://www.youtube.com/watch?v='+songdataJson['metadata']['music'][0]['external_metadata']['youtube']['vid'])
    print('\n','Artist:-> '+songdataJson['metadata']['music'][0]['artists'][0]['name'])
