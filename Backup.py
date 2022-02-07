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
print('This program can backup the data of your app, but it depends on whether the data is portable or not (decided by the developer).')
print('Make sure your phone is connected to the computer, the following content should display "xxxxxx device"')
os.system('.\\adb.exe devices')
print('')
# Device Check End

package = input('Please input the package name of your app (for example like com.google.chrome): ')
input('Please open the app that you want to backup, then press enter to continue.')
input('A dialog box will appear, please click the correct choice depends on your need. Press enter then operate on your phone.')
os.system('.\\adb.exe backup -f .\data\{0}.ab {0}'.format(package))
input('Completed! The data has been saved in the data folder. Press enter to exit.')