#!/bin/bash

# Define a function called fstart
fstart() {
  uvicorn fastapi_ex:pe_urfu --reload --host=10.10.10.59
}  # Start the UVicorn server for the FastAPI application with specified reload and host options

# Define a function called fstop
fstop() {
  uvicorn_pid=`lsof -i :8000 | cut -d' ' -f2`   # Use lsof to find the process ID (pid) of the process using port 8000 and store it in uvicorn_pid
  kill -9 $uvicorn_pid   # Terminate the process with the identified pid using the kill command with signal 9 (SIGKILL)
}

# Define a function called frestart
frestart() {
  fstop   # Call the fstop function to stop the running server
  fstart  # Call the fstart function to start the server again
}

case "$1" in
    "start")  fstart $@ ;;  # If the first command-line argument is "start", call the fstart function with any additional arguments
    "stop") fstop $@ ;;  # If the first command-line argument is "stop", call the fstop function with any additional arguments
    "restart") frestart $@ ;;  # If the first command-line argument is "restart", call the frestart function with any additional arguments
esac

