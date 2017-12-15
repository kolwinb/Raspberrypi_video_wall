#!/bin/bash

path=$(cat path.tmp) 
#echo "$path"
lxterminal -e "cvlc stream://$path --sout '#standard{access=udp,mux=ts,dst=239.0.1.23:1234}'"
