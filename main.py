#Have fun :)

import requests

def lookup_ip(ip):
    url = f"https://geo.proxyspace.pro/ip/{ip}"
    response = requests.get(url)
    data = response.json()
    if 'ip' in data:
        print(f"IP Address: {data['ip']}")
    else:
        print(f"Unable to retrieve data for {ip}")
    print(f"Country: {data.get('country')}")
    print(f"City: {data.get('city')}")
    print(f"Latitude: {data.get('latitude')}")
    print(f"Longitude: {data.get('longitude')}")
    print(f"Postal Code: {data.get('postal_code')}")
    print(f"Time Zone: {data.get('time_zone')}")
    print(f"ASN Number: {data.get('asn_number')}")
    print(f"ASN Organization: {data.get('asn_organization')}")

while True:
    print("1 -> Lookup your own IP address")
    print("2 -> Mass Lookup by file")
    print
    user_input = input("[>] ")

    if user_input == '1':
        url = 'https://geo.proxyspace.pro/ip'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            continue

        data = response.json()
        lookup_ip(data['ip'])
        break
    elif user_input == '2':
        filename = input("Enter the filename list: ")
        try:
            with open(filename) as f:
                for line in f:
                    ip = line.strip()
                    print
                    lookup_ip(ip)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            continue
        break
    else:
        print("Invalid input. Please try again.")

