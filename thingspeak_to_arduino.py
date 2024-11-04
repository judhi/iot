import requests  # using requests module
import time # using time module
import serial # using pyserial module

# function to read field value from Thingspeak
def get_field_value(api_key, channel_number, field_no):
    try:
        url = f"https://api.thingspeak.com/channels/{channel_number}/fields/{field_no}.json?api_key={api_key}&results=1"
        response = requests.get(url)
        data = response.json()
        field_value = data['feeds'][0][f'field{field_no}']
        return field_value
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    api_key = "XB2FXMFTWGOS7FTQ"  # Replace with your own ThingSpeak channel READ API key
    channel_number = 2722700       # Replace with your own ThingSpeak channel number
    
    # Set up serial communication on COM4
    ser = serial.Serial('COM4', 9600) # Replace COM4 with your own serial port number where Arduino is connected
    time.sleep(2)  # Wait for the serial connection to initialize
    
    try:
        while True:
            # Get the fields value
            field_value1 = get_field_value(api_key, channel_number, 1)
            field_value2 = get_field_value(api_key, channel_number, 2)
            if field_value1 is not None and field_value2 is not None:
                print(f"Value of 'field1': {field_value1}")
                print(f"Value of 'field2': {field_value2}")
                # Send field_value to serial port as string with newline and carriage return
                ser.write((str(field_value1) + '\r\n').encode())
            else:
                print("Failed to retrieve data.")
            
            time.sleep(5)  # Wait for 5 seconds before the next request
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        ser.close()  # Close the serial connection when done
