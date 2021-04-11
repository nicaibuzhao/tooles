# 实现思路：以读的方式打开原文件,以写的方式打开一个临时文件,一行行读取原文件内容,修改完后写入临时文件...,删掉原文件,将临时文件重命名原文件名
# 优点: 不会占用过多的内存
# 缺点: 在文件修改过程中同一份数据存了两份
import os


def replace_file(f_path, rf_path, f_str, rf_str):
    """
    :param f_path: 源文件
    :param rf_path: 临时文件  .文件名.swap
    :param f_str: 想要修改的字符串
    :param rf_str: 修改后的字符串
    :return:
    """
    with open(f_path, mode='rt', encoding='utf-8') as read_f, \
            open(rf_path, mode='wt', encoding='utf-8') as wrife_f:
        for line in read_f:
            wrife_f.write(line.replace(f_str, rf_str))

    os.remove(f_path)
    os.rename(rf_path, f_path)
    return "文件修改成功"


replace_file('db.txt', 'db.txt.swap', '一代天骄', '33333')
