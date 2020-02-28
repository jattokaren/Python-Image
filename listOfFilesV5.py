import os
import datetime
#from datetime import datetime
import base64
import csv

directory="/Users/joeat/Documents/Python/Screenshots"
files = list()   #Empty list for filenames + attributes about the file in a dictionary
id = 0

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
#      print(os.path.join(directory, filename))
      print(filename)                                   #see filename
      size = os.path.getsize(directory+'/'+filename)
      print(size)                                       #see file save in bytes

      createDT = str(datetime.datetime.fromtimestamp(os.path.getctime(directory+'/'+filename)))
      print(str(createDT))                              #see file Create Date

      with open(directory+'/'+filename,"rb") as image_file:
        my_string = base64.b64encode(image_file.read())
      print(my_string[:10] + my_string[-10:])           #Base64 Encoded String

      id=id+1
      #files.append({'ID':id, 'Filename':filename, 'Bytes':size}) #Works!!!
      files.append({'ID':id, 'Filename':filename, 'Bytes':size,
      'Create DateTime':createDT,
      'Base64':my_string[:10] + my_string[-10:], 'Base64 Length':len(my_string)}) #Works!!!
      #files.append({'Base64':my_string[:10] + my_string[-10:], 'Base64 Length':len(my_string)})
      with open('file.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, lineterminator='\n',quoting=csv.QUOTE_ALL)
        wr.writerow(files)
      continue
    else:
      continue

#List of Dictionaries to .csv file
#csv_columns = ['ID','Filename','Bytes','Create DateTime','Base64','Base64 Length']   #Needs to match Dictionary Keys
csv_columns = list(files[0].keys())     #Returns Dictionary Keys as a List
dict_data = files
csv_file = "Files.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(files)                                #see list of dictionaries
print(files[0])                             #see 1st dictionary in list
print(files[1])                             #see 2nd dictionary in list
