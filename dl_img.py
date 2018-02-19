import urllib.request

url = input("Enter img url to download: ")
file_name = input("save as: ")

#Download function
def dl_jpg(url, file_path, file_name):
	full_path = file_path + file_name + '.jpg'
	
	urllib.request.urlretrieve(url, full_path)


dl_jpg(url, 'images/', file_name)
