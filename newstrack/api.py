import http.client, urllib.parse
import json

def find_articles(search_term, api_key, start_date, end_date):
    conn = http.client.HTTPSConnection('api.thenewsapi.com')
    params = urllib.parse.urlencode({
        'api_token': api_key,
        'search': search_term,
        'published_after': start_date,
        'published_before': end_date,
    })
    conn.request('GET', '/v1/news/all?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    conn.close()
    
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    return data_dict.get('meta', {}).get('found', 0)