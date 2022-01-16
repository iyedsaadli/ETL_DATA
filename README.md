# ETL_DATA
## An ETL means Extract (get from a source ) -> Transform (filter / clean / change ...) -> Load (save).
### Our first step the is the Extraction process, to get in the program we need to retrieve a zipped csv file from an URL and save it locally.
### Then Unzipp the file or extract data from it directly.
#### To get data from a URL the process is called web scraping, so we're going to send an HTTP request to the URL and GET the data.
    
    url_data = "http://*****.com/file.zip"
    response = requests.get(url_data)
    my_data = resonse.content

### To get data form the Zipfile we need the ZipFile class that return a list of files inside the zipfile.
## READ Files
### 1 ] using pandas 
      file_csv = pd.read_csv("file path")  ## as csv format
      #file_excel = pd.read_excel("file path") ## as excel format
      #file_json = pd.read_json("file path") ## as json format
      #file_html = pd.read_html("file path") ## as html format
      #file_localClipboard = pd.read_clipboard("file path") ## as clipboard format
      #file_MSExcel = pd.read_excel("file path") ## as excel format
      #file_HDF5 = pd.read_hdf("file path") ## as hdf5 fomrmat
      #file_Feather = pd.read_feather("file path") ## as feather format
      #file_msgpack = pd.read_msgpack("file path") ## as msgpack format
### 2 ] READ CSV using csv library
      import csv
      rows = []
      with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
          rows.append(row)
         
### 3 ] USE TEMPORARY FILES TO STORE DATA TEMPORARY DURING PROGRAM EXECUTION
      
      import tempfile
      temp = tempfile.TemporaryFile()
      temp.write(b"foo bar")
      # set the pointer at the starting of the page
      temp.seek(0)
      data = temp.read()
      temp.close()
