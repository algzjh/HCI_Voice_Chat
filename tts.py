# -*- coding: utf-8 -*-
from aip import AipSpeech

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

def text2Mp3(msg, id, my_per, my_vol, my_sdp, my_pit):
    filename = './audio/audio' + str(id) + '.mp3'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(msg, 'zh', 1, {'spd':  my_sdp, 'pit: ': my_pit, 'vol': my_vol, 'per': my_per})
    if not isinstance(result, dict):
        with open(filename, 'wb') as f:
            f.write(result)
    return filename


