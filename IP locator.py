import requests

def kordy(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        latitude = data['lat']
        longitude = data['lon']
        return latitude, longitude
    else:
        return None

while True:
    ip_address = input("Enter an IP address: ")
    
    
    cords = kordy(ip_address)
    
    if cords:
        print(f"Geographic coordinates for your IP")
        print(f"{cords[0]} ; {cords[1]}")
       
    else:
        print("Failed to obtain coordinates for the provided IP address.")
