# House Monitor

---

## Configure enviroment

1. Execute following two commands to update both the package list and installed packages.

```bash
sudo apt-get update
```

and then

```bash
sudo apt-get upgrade
```

2. Install both python3-dev and python3-pip by running the command below.

```bash
sudo apt-get install python3-dev python3-pip
```

4. Install the DHT library, we should first run the following command to ensure we have the latest versions of the setuptools, wheel and pip python packages.


```bash
sudo python3 -m pip install --upgrade pip setuptools wheel
```

5. Now using pip, we will go ahead and install [Adafruit’s DHT library](https://github.com/adafruit/DHT-sensor-library) to the Raspberry Pi.
We will be using this Python library to interact with our DHT22 Humidity/Temperature sensor.
As a bonus, the library also supports the DHT11 and AM2302 humidity/temperature sensors making it a great library to learn how to utilize.
Run the following command to install the DHT library to your Raspberry Pi.

```bash
 sudo pip3 install Adafruit_DHT
```

## Run script

- To run execute the following command.

```bash
 python3 sensor_process.py
```


