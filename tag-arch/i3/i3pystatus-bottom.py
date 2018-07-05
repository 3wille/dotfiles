# -*- coding: utf-8 -*-

import subprocess
import os
import re

from i3pystatus import Status

status = Status(standalone=True)

green  = "#9BEE47"
red    = "#C75646"
yellow = "#FFE377"
white  = "#F7F7F7"
grey = "#AAAAAA"

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week

status.register("clock",
        format="KW%V: %a %-d %b %H:%M",
	interval=30,
)


#status.register("file",
#        components = { "fanout": (int, "sys/devices/platform/applesmc.768/fan1_input") },
#        format = " {fanout} RPM")

status.register("temp",
        format="{temp:.0f}°C",)

status.register("backlight",
        format="{percentage:.0f}%",
        backlight="intel_backlight",
        interval=1)

#status.register("alsa",
#        format=" {volume}%",
#        format_muted=" muted",
#        card = 1
#        )

status.register("pulseaudio",
        format="{selected}{volume}%",
        format_muted="{selected}muted",
        color_muted=grey,
        sink="alsa_output.pci-0000_00_1b.0.analog-stereo"
        )

status.register("pulseaudio",
        format="{selected}{volume}% HDMI",
        format_muted="{selected}muted HDMI",
        color_muted=grey,
        sink="alsa_output.pci-0000_00_03.0.hdmi-stereo"
        )

status.register("pulseaudio",
        format="{selected}{volume}% USB",
        format_muted="{selected}muted USB",
        color_muted=grey,
        sink="alsa_output.usb-Logitech_Logitech_G35_Headset-00.analog-stereo"
        )

status.register("battery",
        format="{status} @{consumption}W: {percentage:.2f}% {remaining:%E%hh:%Mm}",
        alert=True,
        alert_percentage=5,
        status={
            "DIS":  "  Discharging",
            "CHR":  "  Charging",
            "FULL": "⚡ Fully charged",
        },
        full_color=green,
        critical_color=red,
        charging_color=white,
	interval=10,
    battery_ident = "BAT0"
)

status.run()
