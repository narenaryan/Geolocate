import requests

class geolocate():
	
	google_url='https://maps.googleapis.com/maps/api/geocode/json'
	
	def __init__(self,addr):
		#Url that returns geolocation of a place or address
		payload={'sensor':'false','address':addr}
		self.res=requests.get(self.google_url,params=payload).json()

	def data(self):
		try:
			for d in self.res['results'][0]['address_components']:
				print d['types'][0],'==>',d['long_name']
		except:
			print 'fetching data failed'

	def address(self):
		return self.res['results'][0]['formatted_address']

	def lat(self):
		return self.res['results'][0]['geometry']['location']['lat']

	def lang(self):
		return self.res['results'][0]['geometry']['location']['lng']

	def bounds(self):
		print "Surrounding Geometry"
		print 'NorthEast','=>','(',self.res['results'][0]['geometry']['bounds']['northeast']['lat'],',',self.res['results'][0]['geometry']['bounds']['northeast']['lng'],')'
		print 'Southwest','=>','(',self.res['results'][0]['geometry']['bounds']['southwest']['lat'],',',self.res['results'][0]['geometry']['bounds']['southwest']['lng'],')'


if __name__=='__main__':
	g=geolocate('newyork')
	g.data()
	print g.address()
	print g.lat()
	print g.lang()
	g.bounds()






