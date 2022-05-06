# File-Handling-Using_Python


* Python has several functions for creating, reading, updating, and deleting files.
* Python too supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. 
  The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, 
  but like other concepts of Python, this concept here is also easy and short.
  

Working of open() function
__________________________

Before performing any operation on the file like read or write, first we have to open that file. For this, we should use Python’s inbuilt function open().
But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

        f = open(filename, mode)
        
Where the following mode is supported: r , w , a , r+ , w+ , a+ .

      r - file.read()         --open an existing file for a read operation.
      w - file.write()        --open an existing file for a write operation.
      a - file.write()        --open an existing file for append operation.
      
      r+:  To read and write data into the file. The previous data in the file will not be deleted.
      w+:  To write and read data. It will override existing data.
      a+:  To append and read data from the file. It won’t override existing data.
