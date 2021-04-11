from datetime import date

# print(date.max) # date对象所能表示的最大日期
# print(date.min) # date对象所能表示的最小日期
# print(date.resolution) # date对象表示的最小单位，天
# print(date.today()) # 返回一个表示当前本地日期的date对象
# print(date.fromtimestamp(1618059772.8423731)) # 根据指定的时间戳，返回一个date对象


# from datetime import *
#
# now = date(2016, 10, 26)           # date对象
# tomorrow = now.replace(day = 27)   # 生成一个新的日期对象，可指定年月日代替原有属性。原有属性不变
# print(f"now:{now},tomorrow:{tomorrow}")
# print(f"timetuple():{now.timetuple()}")  # 返回日期对应的time.struct_time对象（结构化日期对象）
# print(f"weekday():{now.weekday()}") # 返回weekday，星期一：0，星期二：1 ---以此类推（国外日期）
# print(f"isoweekday():{now.isoweekday()}") # 返回weekday，星期1：1，星期二：2 ---- 以此类推（国内日期）
# print(f"isocalendar():{now.isocalendar()}") # 返回格式（year,month,day）的元组
# print(f"isoformat():{now.isoformat()}") # 返回格式化日期字符串，固定格式：'YYYY-MM-DD’
# print(f"strftime():{now.strftime('%Y-%m-%d')}") # 格式化日期


import datetime

# 输入日期返回星期几
def get_weekday(date):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    return f"{date}是星期{date_obj.isoweekday()}"


print(get_weekday("2021-04-10"))
