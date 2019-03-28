while :
  do
  sudo python ./temp_ds18b20.py
  sudo python ./pres_bmp280.py
  sudo python ./humi_dht11.py
  sleep 1
done
