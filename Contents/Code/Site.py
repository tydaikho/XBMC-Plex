VIDEO_PREFIX = "/video/xbmc"
NAME = "XBMC"

LATEST_VERSION_URL = 'https://bit.ly/xoGzzQ'

# Plugin interest tracking.
VERSION = "1.0"
VERSION_URLS = {
	
	"1.0" : "https://github.com/gparker23/letmewatchthis"
}

FEATURED_ICON='featured.png'
GENRE_ICON='genres.png'
AZ_ICON='atoz.png'

ADDITIONAL_SOURCES = ['icefilms']

def GetGenres():

	return [
		"Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama",
		"Family", "Fantasy", "History", "Horror", "Japanese", "Korean", "Music", "Musical", "Mystery",
		"Romance", "Sci-Fi", "Short", "Sport", "Thriller", "War", "Western", "Zombies"
	]
	
def GetSections(type, genre):

	type_desc = "Movies"
	if (type == "tv"):
		type_desc = "TV Shows"
		
	sections = [
		{ 
			'title': 'Popular',
			'summary': "List of most popular " + type_desc,
			'icon': R("Popular.png"),
			'sort': 'views',
			'type': 'items',
		},
		{
			'title': 'Featured',
			'summary': "List of featured " + type_desc,
			'icon': R(FEATURED_ICON),
			'sort': 'featured',
			'type': 'items',
		},
		{ 
			'title': 'Highly Rated',
			'summary': "List of highly rated " + type_desc,
			'icon': R("Favorite.png"),
			'sort': 'ratings',
			'type': 'items',
		},
		{
			'title': 'Recently Added',
			'summary': "List of recently added " + type_desc,
			'icon': R("History.png"),
			'sort': 'date',
			'type': 'items',
		},
		{
			'title': 'Latest Releases',
			'summary': "List of latest releases",
			'icon': R("Recent.png"),
			'sort': 'release',
			'type': 'items',
		},
	]	
	
	if (not genre):
			
		sections.append(
			{
				'title':"Genre",
				'summary':"Browse " + type_desc + " by genre.",
				'icon':R(GENRE_ICON),
				'type':'genre'
			}
		)
		
		sections.append(
			{
				'title': "A-Z List",
				'summary': "Browse " + type_desc + " in alphabetical order",
				'icon': R(AZ_ICON),
				'type': 'alphabet'
			}
		)
			
		sections.append(
			{
				'type': 'search'
			}
		)
		
	return sections