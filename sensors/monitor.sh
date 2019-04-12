while :
  do
  sudo python /home/pi/dev/balloonPie/sensors/temp_ds18b20.py
  sudo python /home/pi/dev/balloonPie/sensors/pres_bmp280.py
  sudo python /home/pi/dev/balloonPie/sensors/humi_dht11.py
  sudo python /home/pi/dev/balloonPie/sensors/temp_inside.py
  sleep 5
done
