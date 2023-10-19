import json
import requests

def main():
    # load Pace's weather data
    choate_json = json.loads(requests.get('https://colabprod01.pace.edu/api/influx/sensordata/Alan/delta?days=7').text)
    # write your code here



    return

if __name__ == '__main__':
    main()