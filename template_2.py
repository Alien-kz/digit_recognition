import telebot     # run telegram bot

from datetime import datetime # generate log


def log(text):
    time_stamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    print(time_stamp + " " + text)


tasks = dict() #tasks[user] = [1, 5, 4, 2, 3]


if __name__ == "__main__":
    with open("creds/digits_2021_dataset_bot.txt", "r") as f:
        audio_digits_dataset_creds = f.read().strip() # "  hello world \t\n" -> "hello world"
    bot = telebot.TeleBot(audio_digits_dataset_creds)
    print(audio_digits_dataset_creds)

    @bot.message_handler(content_types=['text']) # decorator
    def get_text_messages(message):
        global tasks
        ...
        
        if user not in tasks:
            tasks[user] = random generate
        answer = ... tasks[user]
        send(answer)
        ...


    @bot.message_handler(content_types=['voice']) # decorator
    def get_voice_messages(message):
        user_id = message.from_user.id
        user_name = message.from_user.username

        if not message.voice:
            answer = "Send voice"
            bot.send_message(user_id, answer)
            return

        if user not in tasks:
            tasks[user] = random generate
            answer = ... tasks[user]
            send(answer)
            return

        log_text = "User ({0}): {1}".format(user_name, str(message.voice))
        log(log_text)


        tele_file = bot.get_file(message.voice.file_id)
        log_text = "User ({0}): {1}".format(user_name, str(tele_file))
        log(log_text)

        ogg_data = bot.download_file(tele_file.file_path)
        
        fname = ...tasks[user]
        with open("data/{fname}.ogg".format(fname=fname), "wb") as f:
            f.write(ogg_data)
        
        # remove tasks[user]


        answer = "SAVE FILE LOCAL"
        bot.send_message(user_id, answer)


    bot.polling(none_stop=True, interval=0)


