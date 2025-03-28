#!/bin/bash
   pkg update -y
   pkg upgrade -y
   pkg install python git php wget -y
   pip install requests
