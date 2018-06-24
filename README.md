#  MetadataFixer
Fixes the Metadata of audio files on local machine. Uses Spotipy, acrcloud

<b>Instructions</b>

- Execute Core/acrReco.py
- Select the directory containing the audio src_files
- Supports .mp3, .m4a, .flac

<b> Disclaimer</b>
- Still in development stage
- Take a backup of your Data
- Report any bugs if found :)


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
