from __future__ import unicode_literals
import os
import youtube_dl


def download(df):
	os.chdir('videos/')
	ydl_opts={}

	for url in df['link']:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
