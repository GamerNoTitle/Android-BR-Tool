import os
print('初始化中……')
# Initalize Start
os.system('.\\adb.exe kill-server')
if not os.path.exists('./data'):
    os.system('mkdir data')
os.system('.\\adb.exe start-server')
print('初始化完成！')
# Initalize End

# Device Check
print('')
print('*' * 50)
print('请确认下面是否显示为"xxxxxx device"，如果不是，请确认手机已经打开adb调试并且连接到电脑！')
os.system('.\\adb.exe devices')
print('')
# Device Check End

package = input('请输入要恢复的应用包名: ')
file = input('请输入数据文件位置: ')
print('我们会先备份你的应用数据，以防误操作。')
input('接下来，当你按下回车后，你的手机上会出现提示框，请按需点击！按下回车继续……')
os.system('.\\adb.exe backup -f .\data\{0}-BE-AWARE-OF-IDIOT.ab {0}'.format(package))
print('备份完成，我们现在将进行数据恢复。')
input('接下来，当你按下回车后，你的手机上会出现提示框，请按需点击！按下回车继续……')
os.system('.\\adb.exe restore {}'.format(file))
input('恢复完成，按下回车结束……')
