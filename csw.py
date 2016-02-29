# hit CSW until it says there are no records
import datetime
import time
import urllib
import xml.dom.minidom as minidom

csw_url="http://dev.portal.geoscience.gov.au/geonetwork/srv/eng/csw-australian-topography-featured?SERVICE=CSW&REQUEST=GetRecords&version=2.0.2&resultType=results&maxrecords=50"

num_results = 1

while num_results != 0:
    response = urllib.urlopen(csw_url)
    csw_doc = response.read()
    xml_response = minidom.parseString(csw_doc)
    search_results=xml_response.getElementsByTagName("csw:SearchResults")[0]
    num_results=int(search_results.getAttribute("numberOfRecordsMatched"))
    print num_results
    print time.asctime(time.localtime(time.time()))
    #print datetime.datetime(time.localtime(time.time()))
    time.sleep(300)