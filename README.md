# max_concurrent_video_plays
# Function to find the maximum number of video plays that were playing concurrently 

The main script/function to use is called "max_concurrent_video_plays.py" . This only uses one imported library "json" to read the data.
The source data is stored in source_data.json, this was created using the script called "source_data_generator.py"

I've also add a SQLite3 version "max_concurrent_video_plays_sqlite3.py". This is far faster, but not ideal for a production environment, as it could be leveraged for sql injection (hard coded sql query). It's way more efficient though, but I would not put this into production as it is. I'd add query parameters and totally avoid using a static sql block. 

