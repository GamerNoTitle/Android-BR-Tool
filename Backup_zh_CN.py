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

package = input('请输入要备份的应用包名 (例如com.google.chrome): ')
input('接下来，当你按下回车后，你的手机上会出现提示框，请按需点击！按下回车继续……')
os.system('.\\adb.exe backup -f .\data\{0}.ab {0}'.format(package))
input('备份完成！数据已经保存在data文件夹中，按下回车结束……')
