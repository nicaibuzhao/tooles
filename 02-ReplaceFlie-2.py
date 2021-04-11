# 实现思路：将文件内容发一次性全部读入内存,然后在内存中修改完毕后再覆盖写回原文件
# 优点: 在文件修改过程中同一份数据只有一份
# 缺点: 会过多地占用内存

def replace_file(f_path, f_str, rf_str):
    with open(f_path, mode='rt', encoding='utf-8') as f:
        data = f.read()

    with open(f_path, mode='wt', encoding='utf-8') as f:
        f.write(data.replace(f_str, rf_str))

    return '文件修改成功'
