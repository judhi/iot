# Python code to read data from serial port
# and send it to Thingspeak
# Judhi Prasetyo 2020
import serial # using serial library
import datetime # using date time library
import urllib3 # using urllib3 to send http
# use this command from OS prompt to install urllib3:
# py -m pip install urllib3
ser = serial.Serial('COM4',9600) # open serial port, change to yours!
ser.flushInput()
baseURL = 'https://api.thingspeak.com/update?api_key=' # base Thingspeak URL
API_key = '0HP2GS1A0C39XXX7' # use your own Write API
ID = 'M0000000' # use your own MISIS

while True:
    try:
        ser_bytes = ser.readline() # read one line from serial port
        # and grab the data
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        now = datetime.datetime.now() # create timestamp
        now = now.strftime("%Y-%m-%d %H:%M:%S") # put on readable format
        data = ( "'{}',{}\r\n".format(now,decoded_bytes) ) # prepare data to write
        print(data) # display it on screen
        # preparing URL request with Write API and data
        tsURL = ( "{}{}&field1={}&field2={}".format(baseURL,API_key,ID,decoded_bytes))
        http = urllib3.PoolManager()
        # sending HTTP request to Thingspeak
        tspeak = http.request('GET', tsURL)
        # getting the status
        tspeak.status
    except:
        print("Keyboard Interrupt") # keep looping until user press CTRL-C
        break
