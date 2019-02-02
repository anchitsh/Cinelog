import argparse
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = ''
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
	developerKey=DEVELOPER_KEY)

	search_response = youtube.search().list(
		q=options,
		type='video',
		part='id,snippet',
		maxResults=2
	).execute()

	search_videos = []

	# Merge video ids
	for search_result in search_response.get('items', []):
		search_videos.append(search_result['id']['videoId'])
	video_ids = ','.join(search_videos)

	retur = []

	for i in search_videos:
		yt = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id=" + i + "&key=" + DEVELOPER_KEY
		r = requests.get(url = yt)
		data = r.json()
		retur.append(data)

	return retur

'''
views = data['items'][0]['statistics']['viewCount']
likes = data['items'][0]['statistics']['likeCount']
dislikes = data['items'][0]['statistics']['dislikeCount']
return 
print 'Videos: ' , i, ' views: ', views, ' likes: ', likes, ' dislikes: ', dislikes
'''
