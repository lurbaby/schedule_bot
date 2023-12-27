# Layer 1
FROM ubuntu

# Layer 2
RUN echo "start"



# Layer 3

# COPY hello.py  /


RUN apt-get update && \
    apt-get install -y python3  && \
    apt-get install -y python3-pip


RUN apt-get install -y git

RUN git clone https://github.com/lurbaby/schedule_bot.git



RUN pip install beautifulsoup4 && \
    pip install pyTelegramBotAPI && \
    pip install requests  && \
    pip install lxml


ENTRYPOINT ["python3", "/schedule_bot/direct_bot.py"]


