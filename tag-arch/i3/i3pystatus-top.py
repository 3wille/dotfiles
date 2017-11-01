# -*- coding: utf-8 -*-

import subprocess
import os
import re

from i3pystatus import Status
from i3pystatus.updates import pacman

status = Status(standalone=True)

green  = "#9BEE47"
red    = "#C75646"
yellow = "#FFE377"
white  = "#F7F7F7"
grey   = "#FFFFFF"

status.register("updates",
                format = "Updates: {count}",
                format_no_updates = "",
                interval=120,
                backends = [pacman.Pacman()])

status.register("swap",
        format="swap: {percent_used}",
        warn_percentage=10,
        alert_percentage=30)

status.register("mem",
        format=" {percent_used_mem:.0f}% ({used_mem:.0f}MB/{total_mem:.0f}MB)",
        warn_color = yellow,
        alert_color = red,
#        color = white,
	interval=20
)

status.register("cpu_usage",
        format=" {usage:02}%",
	interval=3
)



#status.register("net_speed",
#                units="B",
#                format="{speed}",
#                interval=5,
#                )

status.register("shell",
         command="python ~/.i3/getip.py",
#         color= white,
         error_color=red,
         interval=5)



status.register("network",
        interface="enp0s25",
        format_up=" {v4}",
        color_up=grey, #green,
        format_down="",
        color_down=red)

        #if (re.findall(r'".*"', os.popen("iwgetid wlp2s0").read())[0] == '""'):
#        wififormat="WiFi down"
#        wificolor = "#FF0000"
#else:
#        wififormat = "WIFI: {essid} with {v4}"
#        wificolor = "#00FF00"

status.register("network",
        interface="wlp4s0",
        format_up=" {essid} ({quality:02.0f}%) {v4}",
        format_down="",
        color_up = grey, #green,
        color_down = red,
        detached_down=True,
        ignore_interfaces=["lo","enp0s25"])

#status.register("network",
#        interface="enp0s20u2",
#        format_up=" {v4}",
#        color_up=green,
#        format_down="down",
#        color_down=red)

status.register("network",
        interface="ppp0",
        format_up=" {v4}",
        color_up=green,
        format_down="",
        color_down=red,
        unknown_up=True,
        ignore_interfaces=["lo","enp0s25","wlp4s0"])

status.register("network",
        interface="tun0",
        format_up=" {v4}",
        color_up=green, 
        format_down="",
        color_down=red,
        unknown_up=True,
        ignore_interfaces=["lo","enp0s25","wlp4s0"])

status.register("keyboard_locks",
                caps_off="",
                interval=0.5,
                format="{caps}"
                )


status.run()
