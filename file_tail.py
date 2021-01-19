def file_tail(filename): 
    """
    This function reads the last 10 lines in a file.

    @param: String - filename
    @return: List
    """

    import os

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
            
            # Read in lines in the file.
            while True: 
                count += 1
                  
                # Update cursor position.
                f_handle.seek(file_size-buffer_size * count) 
                # Update list lines.
                lines.extend(f_handle.readlines()) 
                # Extract the last 10 lines.
                if len(lines) >= 10 or f_handle.tell() == 0: 
                    print(''.join(lines[-10:])) 
                    break


def main():
    try: 
        file_tail('elements.txt') 
    except: 
        print('File not found') 


if __name__ == '__main__': 
    main()