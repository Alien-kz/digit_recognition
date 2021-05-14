import telebot     # run telegram bot

from datetime import datetime # generate log


def log(text):
    time_stamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    print(time_stamp + " " + text)


if __name__ == "__main__":
    with open("creds/digits_2021_dataset_bot.txt", "r") as f:
        audio_digits_dataset_creds = f.read().strip() # "  hello world \t\n" -> "hello world"
    bot = telebot.TeleBot(audio_digits_dataset_creds)
    print(audio_digits_dataset_creds)


    @bot.message_handler() # decorator
    def get_text_messages(message):
        print(message)
        user_id = message.from_user.id
        user_name = message.from_user.username

        question = str(message.text)
        answer = str(eval(question))

        log_text = "User ({0}): {1}".format(user_name, question)
        log(log_text)

        bot.send_message(user_id, answer)

    bot.polling(none_stop=True, interval=0)


