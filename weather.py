cityname = raw_input()
citycode = city.get(cityname)
if citycode:
  url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
  content = urllib2.urlopen(url).read()
  
