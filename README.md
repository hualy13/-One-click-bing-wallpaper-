# -一键bing壁纸-

原理：通过每日任务计划和python脚本来设置bing壁纸

使用方法：下载bat和python脚本放在一个文件夹，然后双击bat即可

修改触发器，如：

一次性触发器：
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc once /st 08:00 /sd 2024-05-20
每周触发器：
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc weekly /d MON,TUE,WED /st 08:00
每月触发器：
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc monthly /d 15 /m 1 /st 08:00
用户登录触发器：
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc onlogon
系统启动触发器：
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc onstart
这些命令会创建名为 "Bing Wallpaper Update" 的任务，并根据不同的触发器类型设置任务的执行时间。
