#!/bin/bash


source /home/ubuntu/.virtualenvs/django_telegram/bin/activate

echo 'ACTIVATED django_telegram'


cd  /home/ubuntu/parsing_news_and_send_telegram/scripts/ &&
source /home/ubuntu/parsing_news_and_send_telegram/scripts/run_commands_with_server.sh
