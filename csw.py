# hit CSW until it says there are no records

from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()
http_proxy = os.environ.get('http_proxy')
http = urllib3.proxy_from_url(http_proxy) if http_proxy else urllib3.PoolManager()

proxies = {"http":"http://pc-65024:5865"}
csw_url="http://dev.portal.geoscience.gov.au/geonetwork/srv/eng/csw-australian-topography-featured?SERVICE=CSW&REQUEST=GetRecords&version=2.0.2&resultType=results&maxrecords=50"
csw = BeautifulSoup(urllib.urlopen(csw_url,proxies=proxies))