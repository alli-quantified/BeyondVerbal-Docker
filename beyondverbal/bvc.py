import os

import requests
requests.packages.urllib3.disable_warnings()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to analyze. Include path. ex: testfile.wav",type=str)
args = parser.parse_args()

# Not looking to re-invent the wheel here on the first go-around. If we can
# even get this off the ground, I'll be tickled. We can always refactor
# or change languages later on. Remember, the end game is streaming in near-realtime,
# not daily runs. For now, we'll settle for batch processing to make sure things work.
#
#    Onward! -as

WAV_File = args.file

def getAnalysis(API_Key,WavPath,META_deviceId,META_trwitterId,META_email):
    res = requests.post("https://token.beyondverbal.com/token",data={"grant_type":"client_credentials","apiKey":API_Key})
    token = res.json()['access_token']
    headers={"Authorization":"Bearer "+token}
    pp = requests.post("https://apiv3.beyondverbal.com/v3/recording/start",json={"dataFormat": { "type": "WAV" }, "metadata": { "deviceId": META_deviceId, "trwitterId": META_trwitterId, "email": META_email }},verify=False,headers=headers)
    recordingId = pp.json()['recordingId']
    with open(WavPath,'rb') as wavdata:
        r = requests.post("https://apiv3.beyondverbal.com/v3/recording/"+recordingId,data=wavdata, verify=False, headers=headers)
        return r.json()

def setupEnv():
    return {
        'BV_API_KEY': os.environ.get('BV_API_KEY'),
        'BV_META_trwitterId': os.environ.get('BV_META_trwitterId'),
        'BV_META_deviceId': os.environ.get('BV_META_deviceId'),
        'BV_META_email': os.environ.get('BV_META_email')
    }

ENV_Params = setupEnv()

json = getAnalysis(ENV_Params['BV_API_KEY'],WAV_File,ENV_Params['BV_META_deviceId'],ENV_Params['BV_META_trwitterId'],ENV_Params['BV_META_email'])
print(json)
