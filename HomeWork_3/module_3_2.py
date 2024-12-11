def send_email(message:str, recipient:str, sender = 'university.help@gmail.com'):
    '''Проверка на корректность e-mail отправителя и получателя.
    Проверка на отправку самому себе.
    Проверка на отправителя по умолчанию.'''
    if ('@' not in recipient) or ('@' not in sender):
         return print(' Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    if not recipient.endswith('.com') and not recipient.endswith('ru') and not recipient.endswith('.net'):
         return print(' Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    if not sender.endswith('.com') and not sender.endswith('ru') and not sender.endswith('.net'):
         return print(' Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
    if sender == recipient:
         return print('Невозможно отправить писмо самому себе')
    elif sender == 'university.help@gmail.com':
         return print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient)
    else:
         return print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recipient)

# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')