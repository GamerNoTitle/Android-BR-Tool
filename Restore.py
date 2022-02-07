import os
print('Initalizing...')
# Initalize Start
os.system('.\\adb.exe kill-server')
if not os.path.exists('./data'):
    os.system('mkdir data')
os.system('.\\adb.exe start-server')
print('Initalized!')
# Initalize End

# Device Check
print('')
print('*' * 50)
print('Make sure your phone is connected to the computer, the following content should display "xxxxxx device"')
os.system('.\\adb.exe devices')
print('')
# Device Check End

package = input('Please input the package that you want to restore: ')
file = input('Please input the file that you want to restore (path/file): ')
print('Now we will backup the data of your app first to avoid IDIOT OPERATION.')
input('A dialog box will appear, please click the correct choice depends on your need. Press enter then operate on your phone.')
os.system('.\\adb.exe backup -f .\data\{0}-BE-AWARE-OF-IDIOT.ab {0}'.format(package))
print('Great! We will start restore now.')
input('A dialog box will appear, please click the correct choice depends on your need. Press enter then operate on your phone.')
os.system('.\\adb.exe restore {}'.format(file))
input('Completed! The data should have been restored. Press enter to exit.')