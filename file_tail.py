import os, sys

def file_tail(filename): 
    """
    This function reads the last 10 lines in a file.

    @param: String - filename
    @return: List
    """

    # Initialize variable
    buffer_size = 8192
    count = 0
      
    # Calculating size of file in bytes.
    file_size = os.stat(filename).st_size 
      
    with open(filename) as f_handle: 
        if buffer_size > file_size: 
            # Updating buffer size.
            buffer_size = file_size - 1
            lines = list() 
            
            while True: 
                count += 1
                  
                # Updating cursor a distanct of 'buffer_size * count'  from 
                # the end of file.
                f_handle.seek(file_size - buffer_size * count) 
                # Populating the list lines by reading from cursor position
                # to the end of file.
                lines.extend(f_handle.readlines()) 
                # Extract the last 10 lines.
                if len(lines) >= 10 or f_handle.tell() == 0: 
                    print(''.join(lines[-10:])) 
                    break


def main():

    try: 
        filename = sys.argv[1]
        file_tail(filename) 

    except FileNotFoundError:
        print("File not found!")

    except IndexError:
        print("Please, provide a file name!")

if __name__ == '__main__': 
    main()