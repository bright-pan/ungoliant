'''
Created on Jan 3, 2016

@author: igzo
'''
from src.model.configuration.SiteConfiguration import SiteConfiguration
from src.model.configuration.UrlBasicConfiguration import UrlBasicConfiguration
from src.model.configuration.UrlComplexConfiguration import UrlComplexConfiguration

sites = {}


site_ti = "theindependentsf.com"
start_ti = 'http://www.theindependentsf.com/'
base_ti = 'http://www.theindependentsf.com/event/'
key_ti = '/event/'
basic_conf_ti = UrlBasicConfiguration(start=start_ti, base=base_ti, key=key_ti)
site_conf_ti = SiteConfiguration(site=site_ti, url_config=basic_conf_ti)


site_f = "thefillmore.com"
start_f = 'http://thefillmore.com/calendar/'
base_f = 'http://thefillmore.com/event/'
key_f = 'thefillmore.com/event/'
basic_conf_f = UrlBasicConfiguration(start=start_f, base=base_f, key=key_f)
site_conf_f = SiteConfiguration(site=site_f, url_config=basic_conf_f)


site_cftm = "centerfornewmusic.com"
start_cftm = 'http://centerfornewmusic.com/calendar/'
base_cftm = 'http://centerfornewmusic.com/calendar/'
key_cftm = 'centerfornewmusic.com/calendar/'
basic_conf_cftm = UrlBasicConfiguration(start=start_cftm, base= base_cftm, key=key_cftm)
site_conf_cftm = SiteConfiguration(site=site_cftm, url_config=basic_conf_cftm)

site_dg = 'http://dancersgroup.org/'
start_dg = 'http://dancersgroup.org/events/'
base_dg = 'http://dancersgroup.org/event/'
key_dg = '/event/'
next_url_dg = 'http://dancersgroup.org/events/page/'
complex_conf_dg = UrlComplexConfiguration(start=start_dg, base=base_dg, key=key_dg, following=next_url_dg)
site_conf_dg = SiteConfiguration(site=site_dg, url_config=complex_conf_dg)

site_sffc = 'http://sf.funcheap.com/'
start_sffc = 'http://sf.funcheap.com/events/'
base_sffc = 'http://sf.funcheap.com/'
key_sffc = 'http://sf.funcheap.com/'
next_url_sffc = 'http://sf.funcheap.com/events/page/'
complex_conf_sffc = UrlComplexConfiguration(start=start_sffc, base=base_sffc, key=key_sffc, following=next_url_sffc)
site_conf_sffc = SiteConfiguration(site=site_sffc, url_config=complex_conf_sffc)

site_bs = 'http://www.booksinc.net/'
start_bs = 'http://www.booksinc.net/event'
base_bs = 'http://www.booksinc.net/event/'
key_bs = '/event/'
next_url_bs = 'http://www.booksinc.net/event/2016'
complex_conf_bs = UrlComplexConfiguration(start=start_bs, base=base_bs,key=key_bs,following=next_url_bs)
site_conf_bs = SiteConfiguration(site=site_bs, url_config=complex_conf_bs)

site_dnal = 'https://www.dnalounge.com/'
start_dnal = 'https://www.dnalounge.com/'
base_dnal = 'https://www.dnalounge.com/calendar/'
key_dnal = 'https://www.dnalounge.com/calendar/'
basic_conf_dnal = UrlBasicConfiguration(start=start_dnal, base=base_dnal, key=key_dnal)
b_site_conf_dnal = SiteConfiguration(site=site_dnal, url_config=basic_conf_dnal)

next_url_dnal = 'https://www.dnalounge.com/calendar/2016/0'
complex_conf_dnal = UrlComplexConfiguration(start=start_dnal, base=base_dnal, key=key_dnal, following=next_url_dnal)
c_site_conf_dnal = SiteConfiguration(site=site_dnal, url_config=complex_conf_dnal)

site_cb = 'cityboxoffice.com'
start_cb = 'https://www.cityboxoffice.com/'
base_cb = 'https://www.cityboxoffice.com/eventperformances'
key_cb = 'eventperformances'
basic_conf_cb = UrlBasicConfiguration(start=start_cb, base=base_cb, key=key_cb)
site_conf_cb = SiteConfiguration(site=site_cb, url_config=basic_conf_cb)

site_js = 'engageinteractive.co.uk'
start_js = 'http://engageinteractive.co.uk/'
base_js = 'http://engageinteractive.co.uk/work/'
key_js = 'work'
basic_conf_js = UrlBasicConfiguration(start=start_js,base=base_js,key=key_js)
site_conf_js = SiteConfiguration(site=site_js,url_config=basic_conf_js)

sites[site_ti] = site_conf_ti
sites[site_bs] = site_conf_bs
sites[site_cftm] = site_conf_cftm
sites[site_dg] = site_conf_dg
sites[site_dnal] = b_site_conf_dnal
sites[site_sffc] = site_conf_sffc
sites[site_f] = site_conf_f
sites[site_cb] = site_conf_cb
sites[site_js] = site_conf_js