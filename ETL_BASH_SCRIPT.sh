# This script downloads the file 'web-server-access-log.txt.gz'
# from "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/".

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz

# The script then extracts the .txt file using gunzip.

gunzip -f web-server-access-log.txt.gz

# The .txt file contains the timestamp, latitude, longitude 
# and visitor id apart from other data.

cut -d "#" -f 1-4 web-server-access-log.txt > new_web_server.txt

tr "#" "," < new_web_server.txt > web_server.csv 

# Transforms the text delimeter from "#" to "," and saves to a csv file.
# Loads the data from the CSV file into the table 'access_log' in PostgreSQL database.

echo "\c template1;\Copy access_log from '/home/project/web_server.csv' DELIMITERS ',' CSV HEADER;" | psql --username=postgres --host=localhost

#to verify that the table accesss_log is populated with the data

echo '\c template1; \\SELECT * from access_log;' | psql --username=postgres --host=localhost
