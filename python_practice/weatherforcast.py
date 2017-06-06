from city import city
import urllib2
import json
cityname = raw_input('Search city or zip\n')
citycode = city.get(cityname)
print cityname
if citycode:
    try:
       url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
       content = urllib2.urlopen(url).read()
       data = json.loads(content)
       result = data.get('weatherinfo')
       str_temp = ('%s\n%s ~ %s') % (
           result['weather'],
           result['temp1'],
           result['temp2']
           )
       print str_temp
    except:
        print 'failed to check out'
else:
    print 'City not found'
