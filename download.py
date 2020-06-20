from __future__ import unicode_literals
import os
import youtube_dl


def download(df):
	os.chdir('videos/')
	ydl_opts={}
	
	for hash in df['link']:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(['https://www.youtube.com/watch?v='+ hash])
