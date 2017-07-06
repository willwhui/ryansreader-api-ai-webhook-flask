from flask import Flask, request, render_template
from flask import jsonify
from flask import json
_base_url = 'https://mypals.today/'
_audio_file = 'static/music1.mp3'
class RyansReader(object):
    def handle_request(self, req):
        if req.get("result").get("action") == 'input.unknown':
            data = render_template('fallback.json', base_url=_base_url, audio_file=_audio_file)
            print(data)
            return data, 200
#            data_speech = "<speak> <audio src=\""+_base_url+_audio_file+"\"></audio> </speak>"
#            print(data_speech)
#            return json.dumps({
#				"speech":data_speech, 
#				"data":json.dumps({
#    						"google":json.dumps({
#								"expect_user_response": true,
#								"is_ssml": true
#								})
#						})
#				})

        else:
            data = 'Welcomes from webhook!'
            return json.dumps({"speech": data, "displayText": data}), 200

