class Track:
  def __init__(self, trackname, tracklength):
    self.name = trackname
    self.length = tracklength

  ##  def show(self):
  ##    print(f'Name: \"{self.name}\" | Length: {self.length} minutes')

  def __str__(self):
    return f'Name: \"{self.name}\" | Length: {self.length} minutes'

  def __lt__(self, other):
    return print(self.length < other.length)
  
  def __gt__(self, other):
    return print(self.length > other.length)

  def __eq__(self, other):
    return print(self.length == other.length)
  
  def __le__(self, other):
    return print(self.length <= other.length)

  def __ge__(self, other):
    return print(self.length >= other.length)

  

class Album: 
  def __init__(self, albumname, band):
    self.name = albumname
    self.band = band
    self.tracklist = []

  ##  def get_tracks(self):
  ##    print(f'{self.name}: ')
  ##    for track in self.tracklist:
  ##      track.show()

  def __str__(self):
    printable_tracklist = ''
    for track in self.tracklist:
      printable_tracklist += ('\t' + str(track) + '\n')
    return f'Album name: \"{self.name}\" \nAlbum author: \"{self.band}\"\nTracks: \n{printable_tracklist}'
  
  def add_track(self, trackname, tracklength):
    self.tracklist.append(Track(trackname, tracklength))

  def get_duration(self):
    duration = 0
    for track in self.tracklist:
      duration += track.length
    return duration


def create_audio_collection():
  global album_a
  global album_b 
  album_a = Album('The album A', 'The band A')
  album_b = Album('The album B', 'The band B')


  album_a.add_track('The song one', 1)
  album_a.add_track('The song two', 2)
  album_a.add_track('The song three', 3)

  album_b.add_track('The song four', 4)
  album_b.add_track('The song five', 5)
  album_b.add_track('The song six', 6)

  ##  album_a.get_tracks()
  ##  album_b.get_tracks()

  album_a.tracklist[1] > album_b.tracklist[2]
  album_a.tracklist[1] < album_b.tracklist[2]
  album_a.tracklist[1] == album_b.tracklist[2]
  album_a.tracklist[1] <= album_b.tracklist[2]
  album_a.tracklist[1] >= album_b.tracklist[2]

  print(album_a)
  print(album_b)

create_audio_collection()
print(f'Album A duration: {album_a.get_duration()} mins.')
print(f'Album B duration: {album_b.get_duration()} mins.')

