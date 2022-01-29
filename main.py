from pprint import pprint

from ua_parse import parse_ua

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'

res = parse_ua(ua)

pprint(res)
