import spotipy

class SpotifyController():
     def __init__(self, TOKEN, DEVICEID):
          self.sp = spotipy.Spotify(auth=TOKEN)
          self.device_id = DEVICEID

     def pause(self):
          self.sp.pause_playback(device_id=self.device_id)

     def play(self):
          self.sp.start_playback(device_id=self.device_id)

     def next_track(self):
          self.sp.next_track(device_id=self.device_id)

     def previous_track(self):
          self.sp.previous_track(device_id=self.device_id)
