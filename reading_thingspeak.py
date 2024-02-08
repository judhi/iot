import requests

def get_field_value(api_key, channel_number, field_no):
    try:
        url = f"https://api.thingspeak.com/channels/{channel_number}/feeds.json?api_key={api_key}&results=1"
        response = requests.get(url)
        data = response.json()
        field_value = data['feeds'][0][f'field{field_no}']
        return field_value
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    api_key = "XCALXO6N6F5OZ10J" # change this to your own Thingspeak channel READ API
    channel_number = 2412118  # change this to your own Thingspeak channel number
    field_value1 = get_field_value(api_key, channel_number, 1)
    field_value2 = get_field_value(api_key, channel_number, 2)
    if field_value1 is not None:
        print(f"Value of 'field1':", field_value1)
    if field_value2 is not None:
        print(f"Value of 'field2':", field_value2)
