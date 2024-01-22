## create kill switch remotely using esp8266

To create kill switch remotely, we can setup ESP8266 as an Access Point
We need to add these code into in Arduino IDE under tool -> esp8266 board

## Add the code below:

## Note: change ssid and password according to your details

```
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
 
const char *ssid = "YOUR_SSID";
const char *password = "YOUR_PASSWORD";
 
const char *apIPAddress = "192.168.1.1"; // THIS WILL BE THE IP YOU USE TO DISPLAY THE PAGE IN YOUR BROWSER ONCE CONNECTED TO THE ACCESS POINT
const char *apSubnetMask = "255.255.255.0";
 
const int gpioPin = 2; // THIS IS THE IO-PIN WE WILL BE CONTROLLING. CHECK THE BOARD SCHEMATIC FOR REFERENCE
 
ESP8266WebServer server(80);
 
void setup() {
  Serial.begin(115200);
 
  // Set up the ESP8266 as an access point with a specific IP address
  IPAddress apIP;
  apIP.fromString(apIPAddress);
  WiFi.softAPConfig(apIP, apIP, IPAddress(255, 255, 255, 0));
  WiFi.softAP(ssid);
 
  // IP Address of the ESP8266 in AP mode
  IPAddress apIPResult = WiFi.softAPIP();
  Serial.print("Access Point IP address: ");
  Serial.println(apIPResult);
 
  // Set GPIO pin as output
  pinMode(gpioPin, OUTPUT);
 
  // Define the HTML content
  server.on("/", HTTP_GET, []() {
    String html = "<html><body>";
    html += "<h1>Emergency Killswitch</h1>";
    html += "<form action='/toggle' method='get'>";
    html += "<input type='submit' value='STOP DOING THE THING!!'>";
    html += "</form></body></html>";
    server.send(200, "text/html", html);
  });
 
  // Handle the /toggle URL to toggle the GPIO
  server.on("/toggle", HTTP_GET, []() {
    digitalWrite(gpioPin, !digitalRead(gpioPin));
    server.sendHeader("Location", "/");
    server.send(303);
  });
 
  server.begin();
}
 
void loop() {
  server.handleClient();
  }
```
## Save, run and upload

run by click on ' Serial Monitor '
click 'upload'

## select your sever to connect

## copy ip address to your browser

the image show as picture

<img src="/esp8266/killswitch_on_web.png"/>


click the button to stop and start the switch



