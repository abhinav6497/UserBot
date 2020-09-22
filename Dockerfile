# We're using Ubuntu 20.10
FROM sahyam/docker:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/abhinav6497/UserBot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

CMD ["python3","-m","userbot"]
