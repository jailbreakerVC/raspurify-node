from phew import server, connect_to_wifi
import network
import config
import os 
from neopixel import pixels_fill, pixels_show



#network connecitng
connect_to_wifi(config.WIFI_NAME,config.WIFI_PASSWORD)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip_add=wlan.ifconfig()



#led color config
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)

#handler methods
def ledon(request):
    pixels_fill(RED)
    pixels_show()
    return "gotit",200

def ledoff(request):
    pixels_fill(BLACK)
    pixels_show()
    return "turning off",200

@server.catchall()
def catchall(request):
  return "Not found", 404

#server routes
server.add_route("/on",ledon,methods=["GET"])
server.add_route("/off",ledoff,methods=["GET"])

#starting server
server_url= "http://" + str(ip_add[0])
print(f"running",server_url.replace(" ",""))
server.run(host="0.0.0.0", port=80)


