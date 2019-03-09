from spotify_controller import SpotifyController
import json

auth = json.loads(open('auth.json', 'r').read())
device_id = auth['device_id']
token = auth['token']

sp = SpotifyController(token, device_id)

# Play
sp.play()

# Pause
# sp.pause()

# Next
# sp.next_track()

# Previous
# sp.previous_track()