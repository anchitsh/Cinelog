import datetime
import holidays
import time
import predict
import decay
import operator

def score_mov(mov, watch):
	rating = normalize(mov, 0)
	votes = normalize(mov, 4)
	genres = genre_rate(mov, 3)
	yt = yt_index(mov, 7)

	comp = []
	for i in range(0, 4):
		comp.append(rating[i] + votes[i] + genres[i] + yt[i])
	return comp

def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)

def normalize(movie, ttt):
	least = 0;
	for i in range(0, 4):
		if(movie[i][ttt] < least):
			least = i

	score = []
	for i in range(0, 4):
		score.append(abs(movie[i][ttt] - least))
	return score

def genre_rate(mov, ttt):
	charts = set(["Adventure", "Action", "Drama", "Comedy", "Thriller", "Suspense", "Horror", "Romantic", "Comedy", "Musical", "Documentary", "Black", "Comedy", "Western", "Reality"])
	score = []
	for i in range(0, 4):
		num = len(mov[i][ttt])
		s = 0
		for y in range(0, num):
			if(mov[i][ttt][y] in charts):
				s = s + 1
		score.append(s)
	return score

def yt_index(mov, ttt):
	li = []
	for i in range(0, 4):
		print mov[i][ttt][1]
		score = (float(mov[i][ttt][1])/float(mov[i][ttt][2])) * int(mov[i][ttt][0])
		li.append(score)
	return li

def schedule(scores, m1, m2, m3):
	dcay = [0,]
	for i in [ m1, m2, m3]:
		#predict.predict_done()
		dcay.append(decay.decay(i))

	for i in range(0,4):
		scores[i] = scores[i] * (1 - dcay[i])

	hi = max(scores)
	lo = min(scores)

	for i in range(0,4):
		scores[i] = float(scores[i])/float(hi-lo)

	d = {}

	for i in range(0, 4):
		d[i] = scores[i]

	dx = sorted(d.items(), key=operator.itemgetter(1))

	print [i[1]*12 for i in dx]

def fun(movies, watch):
	d = score_mov(movies, watch)
	schedule(d, movies[1][1], movies[2][1], movies[3][1])