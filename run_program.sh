echo "Запуск скрипта" >> /home/user/bot/log.txt
source /home/user/bot/venv/bin/activate
/home/user/bot/venv/bin/python /home/user/bot/bot.py >> /home/user/bot/log.txt 2>&1
echo "Завершение скрипта" >> /home/user/bot/log.txt

