@echo off
echo Doing tracert at %date%, %time% >> tracer.txt
echo  LOOPING TRACE-ROUTE CONTAINER
tracert 8.8.8.8 
12.bat