import sys
from factors import imdb
from factors import youtube
from factors import hdays
from model import compare
from model import predict

audit = 2

mov_ply = sys.argv[1:5]
seats = sys.argv[5]

temp = [imdb.metadata(mov_ply[0]), imdb.metadata(mov_ply[1]), imdb.metadata(mov_ply[2]), imdb.metadata(mov_ply[3])]

m = []
c = 0

for i in temp:
	m.append([i.rating, i.title, i.year, i.genres, i.votes, i.release_date, i.cast_summary])
	results = youtube.youtube_search(str(i.title + " Trailer"))
	youtube_data = []
	for h in range(0,2):
		data = results[h]
		views = data['items'][0]['statistics']['viewCount']
		likes = data['items'][0]['statistics']['likeCount']
		dislikes = data['items'][0]['statistics']['dislikeCount']
		youtube_data = [views, likes, dislikes]
	m[c].append(youtube_data)
	print m[c][5]
	c = c + 1

watch = hdays.get_holidays(m[0][5])

compare.fun(m, watch)

predict.predict_done()