import requests, sys, socket, json

if len(sys.argv) < 2: 
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

url =  sys.argv[1]

req = requests.get("https://" + url)
print("\n Headers are" + str(req.headers))

host = socket.gethostbyname(url)
print("\n IP address of " + url + " is " + host)

ipinfo = requests.get("https://ipinfo.io/" + host + "/json")
location = json.loads(ipinfo.text)

print("\n Location is " + location["loc"])
print("\n Region is " + location["region"])
print("\n City is " + location["city"])
print("\n Country is " + location["country"])