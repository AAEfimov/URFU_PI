#!/bin/bash

fstart() {
  uvicorn fastapi_ex:pe_urfu --reload --host=10.10.10.59
}

fstop() {
  uvicorn_pid=`lsof -i :8000 | cut -d' ' -f2`
  kill -9 $uvicorn_pid
}

frestart() {
  fstop
  fstart
}

case "$1" in
    "start")  fstart $@ ;;
    "stop") fstop $@ ;;
    "restart") frestart $@ ;;
esac

