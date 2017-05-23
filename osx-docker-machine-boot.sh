#!/usr/bin/env sh

curl -sL http://git.io/vsk46 | \
    sed -e "s?{{docker-machine}}?$(which docker-machine)?" \
        -e "s?{{user-path}}?$(echo $PATH)?" \
    >~/Library/LaunchAgents/com.docker.machine.default.plist && \
    launchctl load ~/Library/LaunchAgents/com.docker.machine.default.plist
