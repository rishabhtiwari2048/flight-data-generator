from faker import Faker
from faker_airtravel import AirTravelProvider
from configparser import ConfigParser
from datetime import datetime
import time
import json
if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.ini')
    fake = Faker()
    fake.add_provider(AirTravelProvider)
    record_count = config.getint('records','records_per_file')
    #print(record_count)
    delay_time = config.getint('records', 'idle_time_files')
    #print(delay_time)
    num_of_files = config.getint('files', 'num_of_files')
    #print(num_of_files)
    file_prefix = config.get('files', 'file_prefix')
    #print(file_prefix)
    destination = config.get('files', 'destination')
    #print(destination)

    for num in range(0,num_of_files):
        file_name = file_prefix+"_"+str(datetime.now()).replace(" ",'').split(".")[0].replace(":","").replace("-","")+".json"
        with open(destination+"/"+file_name,"w",encoding="utf-8") as file:
            for record in range(0,record_count):
                flight_booking = fake.flight()
                json.dump(flight_booking,file,ensure_ascii=False)
                file.write("\n")
        print(f"{file_name} has been written successfully")
        time.sleep(delay_time)







