from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        url = "https://restcountries.com/v3.1/all"
        country = dictionary.get("country")
        capital = dictionary.get("capital")
        
        response = requests.get(url)
        data = response.json()
        
        message = ""
        
        if capital:
            for country_data in data:
                if capital in country_data.get("capital"):
                    country_name = country_data.get("name").get("common")
                    message = f"The capital of {country_name} is {capital}"
                    break
        elif country:
            for country_data in data:
                if country == country_data.get("name").get("common"):
                    capital = country_data.get("capital")[0]
                    message = f" {capital} is The capital of {country}  "
                    break
        else:
            message = "Give me a valid country please"
        
        self.wfile.write(message.encode())
        return
