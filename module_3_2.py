def send_email(message, recipient,*, sender):
    if recipient.find('@') != -1 and sender.find('@') != -1:
        if ((recipient.find('.com') != -1 or recipient.find('.ru') != -1 or recipient.find('.net') != -1)
                and (sender.find('.com') != -1 or sender.find('.ru') != -1 or sender.find('.net') != -1)):
            if sender == 'university.help@gmail.com' and sender == recipient:
                print('Нельзя отправить письмо самому себе')
            elif sender == 'university.help@gmail.com' and sender != recipient:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            return

        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('hellow', 'university.help@gmail.com', sender = 'university.help@gmail.com')