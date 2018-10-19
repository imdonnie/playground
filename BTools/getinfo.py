import subprocess
import win32con
import win32clipboard as w

def inputToChipboard(string):
    w.OpenClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,string)
    w.CloseClipboard()

cmd_get_info = "powercfg /batteryreport"

p = subprocess.Popen(cmd_get_info, 
					  shell=True, 
					  stdout=subprocess.PIPE, 
					  universal_newlines=True)
p.wait()
result_lines = p.stdout.readlines()

raw_battery_info = result_lines[0].split(' ')
raw_battery_path = raw_battery_info[1].replace('。', '')
battery_path = "file:///"+raw_battery_path.replace('\\', '/')

print(battery_path)

cmd_start_edge = "start microsoft-edge"
cmd_view_info = "{0}:{1}".format(cmd_start_edge, battery_path)
print(cmd_view_info)
inputToChipboard(battery_path)
print("on clipboard")
# p = subprocess.Popen("powercfg /batteryreport", 
# 					  shell=True, 
# 					  stdout=subprocess.PIPE, 
# 					  universal_newlines=True)
