with open("C:\\Users\\DELL\\Desktop\\PYTHON\\Reading-Text-Files\\story.txt", 'r') as f:
    for line in f:
        print(line.strip().split())

    f.close()