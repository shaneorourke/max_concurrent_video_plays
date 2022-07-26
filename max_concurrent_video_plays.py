import json
# Function to find the maximum number of video plays that were playing concurrently
# Requirements:
# 1. Accept a finite number of video play records (source_data.json)
# 2. Use only standard python libraries (e.g. No pandas, numpy etc)


# Function to count concurrent plays in json input file: returns start_time of video play and max   
def count_concurrent_video_plays(json_input_filename:str):
    # Loading the json file into a variable
    data = json.load(open(f'{json_input_filename}'))
    # Store the json data with in a dict using comprehesion
    data_dict = {key:{'start_time':data[key]['start_time'],'end_time':data[key]['end_time']} for key in data}
    # Instanciate empty list for storing concurrent plays 
    count_list = []

    # Loop over dictionary
    for item in data_dict.items():
        # Instancia current_start datetime for iteration
        current_start = item[1]['start_time']
        # Loop again over dictionary to see if current_start_time is between another video play start and end time
        for item_inner in data_dict.items():
            # Instanciate inner loops start_time and end_time
            counter_start, counter_end = item_inner[1]['start_time'], item_inner[1]['end_time']
            # If the current_start is between the inner loops start and end
            if current_start >= counter_start and current_start <= counter_end and item[0] != item_inner[0]:
                # Add the current iteration's start_time to count_list list (concurrent play)
                count_list.append(current_start)
    # Set start_time with most concurrent video plays
    max_concurrent_plays = max(count_list,key=count_list.count)
    # Using start_time get the integer of the max concurrent plays
    concurrent_plays_count = count_list.count(max_concurrent_plays)

    # Return only integer of the max concurrent plays
    return concurrent_plays_count


if __name__ == '__main__':
    # If executed within this script print out the result
    # If imported into another python file, ensure that the file path and file name is passed
    # Print out will NOT occur if the above function is imported into another file 
    concurrent_plays_count = count_concurrent_video_plays('source_data.json')
    print(f'concurrent_plays:{concurrent_plays_count}')
