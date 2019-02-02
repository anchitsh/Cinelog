from imdbpie import Imdb
import sys

def metadata(s):
	imdb = Imdb()
	imdb = Imdb(anonymize=True) # to proxy requests
	names = imdb.search_for_title(s)
	title = imdb.get_title_by_id(names[0][u'imdb_id'])
	cast = cast_rating(title.cast_summary)
	return title

def cast_rating(summary):
	print summary[0].imdb_id

# title.title, title.type, title.year, title.rating, title.genres, title.votes, title.runtime, title.release_date, title.cast_summary]