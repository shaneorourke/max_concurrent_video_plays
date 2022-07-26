import json, sqlite3
# Function to find the maximum number of video plays that were playing concurrently
# Requirements:
# 1. Accept a finite number of video play records (source_data.json)
# 2. Use only standard python libraries (e.g. No pandas, numpy etc)

# Function to replace standard syntax output from SQLite3
def sqlite3_output_replace(input:str):
    # Basic sqlite3 returned sytax to remove stored in list
    replace_list = ['(',')',',']
    # Iterate over the above list
    for r in replace_list:
        # Replace each iteration with nothing/empty string
        input = str(input).replace(r,'')
    # Return replaced input
    return input

# Function to count concurrent plays in json input file: returns start_time of video play and max
def count_concurrent_video_plays(json_input_filename:str):
    # Create connection and or local SQLite3 database
    con = sqlite3.connect(f'{json_input_filename}.db')
    # Create conneciton cursor
    cur = con.cursor()
    # If table exists, drop it
    con.execute('DROP TABLE IF EXISTS tvideo_plays')
    # Create new table to house the json input data
    con.execute('CREATE TABLE tvideo_plays (videoplay test, start_time datetime, end_time date_time)')

    # Loading the json file into a variable
    data = json.load(open(f'{json_input_filename}'))
    # Iterate over json data stored in variable
    for row in data:
        # Extract start, end and row (video_play name/id)
        start_time, end_time = data[row]['start_time'],data[row]['end_time']
        # Insert each iteration's row into create table
        cur.execute(f'INSERT INTO tvideo_plays (videoplay, start_time, end_time) VALUES (?,?,?)',(row,start_time,end_time))

    # Commit open transactions
    con.commit()

    # Declare query to be executed. CTE to find concurrent plays (joining to itself between start and end times)
    # Returning max counts for video plays
    query = '''
            with conc_plays as (
	            select p1.start_time from tvideo_plays p1
		            left join tvideo_plays p2
			            on p1.start_time >= p2.start_time
				            and p1.start_time < p2.end_time
                                and not (p1.videoplay = p2.videoplay))
            , max_plays as (select start_time, count(*) as counter from conc_plays group by start_time)
            select max(counter) from max_plays
            '''
    # Execute declared query
    cur.execute(query)
    # Store query results in varible
    result = sqlite3_output_replace(str(cur.fetchone()))
    # Close connection to database
    con.close()

    # Return only database query result
    return result


if __name__ == '__main__':
    # if executed within this script print out the result
    # If imported into another python file, ensure that the file path and file name is passed
    # Print out will NOT occur if the above function is imported into another file 
    concurrent_plays_count = count_concurrent_video_plays('source_data.json')
    print(f'concurrent_plays:{concurrent_plays_count}')
