import json
import requests
import pprint


if __name__ == "__main__":

    def api_get_request(url):
        data = requests.get(url).text;
        data = json.loads(data);
        pp = pprint.PrettyPrinter();
        pp.pprint(data['topartists']['artist'][0]['name']);

        return data


api_get_request('http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=4beab33cc6d65b05800d51f5e83bde1b&format=json')

