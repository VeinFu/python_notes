# *-* coding: utf-8 *-*

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
	'select_favourite_book':{
		'task': 'favourite_book.select_favourite_book',
		'schedule': timedelta(seconds=10),
	},
}
