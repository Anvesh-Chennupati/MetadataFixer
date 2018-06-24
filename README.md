#  MetadataFixer
Fixes the Metadata of audio files on local machine. Uses Spotipy, acrcloud and many more
Create a backup (Recommended)

<b>Creating ACR Cloud Keys</b>
- Install acrcloud_sdk_python
- python -m pip install git+https://github.com/acrcloud/acrcloud_sdk_python

- Audio fingerprinting and metadata fetch from ACR Cloud
- Create a developer account at acrcloud https://ap-console.acrcloud.com/service/avr
- In dashboard select Audio Video Recognization
- Create Project
- Name the Project
- Select Recorded Audio in Audio Source
- Select ACR Cloud Music in Buckets
- Enable 3rd Party Integration and click on Create

- Enter Host, Access key, Access Secret
