import Adafruit_DHT

pinGPIO = 4
sensor = Adafruit_DHT.AM2302


def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pinGPIO)

        if humidity is not None and temperature is not None:
            print(
                "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")


if __name__ == "__main__":
    main()
