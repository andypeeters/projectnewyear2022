FROM python:3
COPY new-years-wishes.txt /
COPY sending-new-years-wishes.py /
CMD [ "python", "-u", "./sending-new-years-wishes.py" ]