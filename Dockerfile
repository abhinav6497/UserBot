# We're using Ubuntu 20.10
FROM abhinav6497/docker:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/abhinav6497/UserBot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/abhinav6497/UserBot/sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
