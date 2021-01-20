# Home-Assistant-config
This repository contains my work-in-progress home Assistant configuration. This is another step in my journey 
to host my photography journey, website, home security, and automations. A lot to learn
for a photographer, but lots of fun, maybe some fustration thrown in for laughs. Many thanks to BreadedThinker for his help and commitment to Synology and Frenck Nijhof and DrZzs for thier introduction to .yaml and other videos.

My Dashboard



# My set up
Synology NAS 918+
- hardware
  - Ram 8 GB
  - SSD Cashe 2 Sandisk 250 GB
  - HHD 4 WDC 3.6 TB
- Storage Pool 
  - RAID 10
  - Capacity 7.27 TB
- External Devices
  - USB hub - Genesys Logic
  - USB drive - LaCie 3.5 TB (system back-up)
  - /dev/ttyACM0 (Z-Wave)
  	- Aeotec Z-Stick Gen5 (ZW090) - UZB- Sigma Designs, Inc.
  - /dev/ttyACM1 (Zigbee)
  	- Texas_Instruments_TI_CC2531_USB_CDC
  - /ip cameras
  	- 4 IP8M-2496E
	- 1 IP8M-2493E
  - /doorbells
  	- 2 Nest Hello
  - /smoke/carbon dioxide detectors
  	- 7 Nest Protect
  - /thermostats
  	- 4 ecobee 3 lite
  - /devices
  	- wi-fi, zigbee, z-wave
  	- 35 combination of outlets, plugs, switches, and sensors
	- 3 Alxas
# Hass.io
- SynoCommuity
	- fredrike=hassio
- Integrations
	- AccuWeather
	- Alexa Media Player
	- Biltzortung
	- ecobee
	- Garbage Collection
	- Garmin Connect
	- Life360
	- MQTT Broker
	- OpenWeatherMap
	- Speedtest
- Addons
	- ESPHome
	- Grafana
	- Grocy
	- Home Panel
	- Mosquito broker
	- Node-RED
	- VS Code
	- Z-Wave to MQTT
	- Zigbee2MQTT Bridge
	- Zigbee2mqee Edge
# Docker Containers
- Influxdb
- Portainer

