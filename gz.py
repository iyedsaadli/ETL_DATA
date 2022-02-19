import gzip

#decompress the gz file

txt = gzip.GzipFile("/home/runner/web-server-access-log.txt.gz", 'rb')
file = txt.read()
txt.close()

#write the data to a file

load = open("/home/runner/my_file.txt", 'wb')
load.write(file)
load.close()
