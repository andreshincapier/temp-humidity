import Adafruit_DHT
import time

pinGPIO = 4
sensor = Adafruit_DHT.AM2302


def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pinGPIO)

        if humidity is not None and temperature is not None:
            print('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))

        else:
            print("Failed to retrieve data from humidity sensor")


if __name__ == "__main__":
    main()
