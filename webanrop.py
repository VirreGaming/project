import requests
import json
while True:
    print("==== Räkna subnät med API ====")
    address_input = input("Ange nät (med prefix: x.x.x.x/yy):")
    address_url = "https://networkcalc.com/api/ip/" + address_input+"?binary=true&fields=[network_address,broadcast_address]"
    response =requests.request("GET", address_url)
    #print(response)
    #print(type(response.text))
    json_object = json.loads(response.text)

    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    print("hämtar data från", address_url)
    print(json_object["address"]["network_address"])