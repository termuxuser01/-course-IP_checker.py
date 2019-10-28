import os
#mathces files whoes name follows some pattern
import fnmatch

#returns a tuple that represents paht to the directory
def find_album(root, artist_name):
  for path, directories, files in os.walk(root):
    #uses fnmatch.filter() to filter out artist results if this line wasn't here line 18 would print out all entries
    for artist in fnmatch.filter(directories, artist_name):
      subdir = os.path.join(path, artist)
      for album_path, albums, _ in os.walk(subdir):
        for album in albums:
          yield os.path.join(album_path, album), album

def find_songs(albums):
  for album in albums:
    for song in os.listdir(album[0]):
      yield song


album_list = find_album("music", "Aerosmith")
song_list = find_songs(album_list)

# for x in album_list:
#   print(x)

for s in song_list:
  print(s)      
