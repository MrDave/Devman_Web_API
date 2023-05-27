import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

ref_link = "https://dvmn.org/referrals/gebYFKqYsPRBwPv1w0hsOwUXckOX9nIMHxN9v2G9/"
friend_name = "Пётр"
my_name = "Давид"

sender = "davidschnoll@gmail.com"
recipient = "davidschnoll+pythonr@gmail.com"
subject = "Приглашение!"
content_type = 'text/plain; charset="UTF-8"'

template = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

letter = template.replace('%friend_name%', '{friend_name}').replace('%my_name%', '{my_name}')\
    .replace('%website%', '{website}')
letter = """\
From: {f}
To: {t}
Subject: {s}
Content-Type: {c} \n
""" + letter
letter = letter.format(website=ref_link, friend_name=friend_name, my_name=my_name, f=sender, t=recipient, s=subject,
                       c=content_type)

letter = letter.encode("UTF-8")

login = os.getenv('MAIL_LOGIN')
password = os.getenv('MAIL_PASSWORD')

server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(login, password)
server.sendmail(sender, recipient, letter)
server.quit()
