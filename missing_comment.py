def missing_comment(file):
    with open(file) as f:
        counter = 1

        for line in f:
            if line.lstrip().startswith('#'):
                comment = True
            elif comment is False and line.startswith('def '):
                func_name = line[line.index(' ')+1:line.index('(')]
                print(f'\nFunction name: {func_name}')
                print(f'File name: {file}')
                print(f'Line number: {counter}')

            else:
                comment = False


            counter += 1


def main():
    
    missing_comment('func2.py')


if __name__ == '__main__':
    main()