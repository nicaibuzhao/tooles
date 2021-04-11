def slice_file(path, lines, slice_name):
    with open(path, 'r') as reader:
        counter = 0  # 控制文件行数
        findex = 0  # 控制文件个数
        for line in reader:  # 读取文件
            if counter == 0:
                writer = open(slice_name + str(findex), 'w')
            writer.write(line.strip() + '\n')
            counter += 1
            if counter >= lines:
                writer.close()
                counter = 0
                findex += 1



slice_file("my-file.txt", 299998, "file-")
