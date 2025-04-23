#File objects

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:    
        for line in rf:
            wf.write(line)


    # f.write('Test')
    # f.seek(0)
    # f.write('TestDWA')



    # size_to_read = 10
    # # for line in f:
    # #     print(line, end='')

    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # print('intersection')
    # f_contents = f.read(20)
    # print(f_contents)
    # f_contents = f.readline()
    # print(f_contents)
    # print(f.read())
# f = open('test.txt', 'r')

# print(f.name)

# f.close()
# print(f.read())
