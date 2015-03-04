# docker run -v /Users/dotMR/repository/race-monitor:/tmp --device /dev/tty.usbserial-A600e0BZ  dotmr/race-monitor

# Note: To list ports (on mac)
#   ls /dev/tty.*
#   ls /dev/cu.*

FROM python:2.7
RUN pip install pyserial

# volume mounted here
WORKDIR /tmp
CMD python src/race-monitor.py
