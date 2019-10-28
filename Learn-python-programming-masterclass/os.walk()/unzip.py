import zipfile

path = ("./music.zip")

zip = zipfile.ZipFile(path)
zip.extractall('.')
zip.close()
