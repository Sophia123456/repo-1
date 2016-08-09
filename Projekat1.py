from lxml import html
import requests

page=requests.get("http://sport.blic.rs/brazil-oi/rio-4-dan-crnogorce-presreli-pljackasi-sok-za-spance-nasi-bez-borbe-za-medalje/s68xlch")
tmpsrv=html.fromstring(page.content)

novinar=tmpsrv.xpath("//span[@class='k_author']/text()")
Rio2016=tmpsrv.xpath("//span[@class='k_noteLead']/text()")

print "Novinar:", novinar 
print "Rio2016", Rio2016
