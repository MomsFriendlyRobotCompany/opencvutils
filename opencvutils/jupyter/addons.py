
try:
	from IPython.display import HTML

	def showVideo(filename, width=None):
		# from IPython.display import HTML
		video = open(filename, "rb").read()
		video_encoded = video.encode("base64")
		if width:
			video_tag = '<video width={} controls src="data:video/x-m4v;base64,{}">'.format(width, video_encoded)
		else:
			video_tag = '<video controls src="data:video/x-m4v;base64,{}">'.format(video_encoded)
		return HTML(video_tag)

except ImportError:
	def showVideo(filename, width=None):
		print('ipython not installed')
