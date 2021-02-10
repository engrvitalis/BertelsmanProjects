def update_file(in_file, out_file):
    with open(in_file) as f:
        for line in f:
            if '<pre>' in line and 'print' in line:
                
                print(line.index('<pre>'))


update_file('example.html', 'out')