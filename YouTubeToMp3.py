from pytube import YouTube
print('Enter the url')
url = input()
YTV = YouTube(url)
YTV.streams.get_highest_resolution().download('place')#in windows use \\
print("ALL downloaded")
