@echo off
title stopAppiumServer
tasklist|find /i "node.exe" ||exit
taskkill /im node.exe /f