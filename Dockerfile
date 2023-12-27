# Layer 1
FROM ubuntu

# Layer 2
RUN echo "start"



# Layer 3
RUN apt-get update && \
    apt-get install -y python3  && \
    apt-get install -y python3-pip

# Layer 4
RUN apt-get install -y git

# Layer 5
RUN git clone https://github.com/lurbaby/schedule_bot.git

# Layer 6
RUN pip install beautifulsoup4 && \
    pip install pyTelegramBotAPI && \
    pip install requests  && \
    pip install lxml

# Layer 7
ENTRYPOINT ["python3", "/schedule_bot/direct_bot.py"]


