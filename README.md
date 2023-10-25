# :computer: Software Engenering Project

[![Update Ubuntu 22.04](https://github.com/AAEfimov/URFU_PI/actions/workflows/python-app.yml/badge.svg)](https://github.com/AAEfimov/URFU_PI/actions/workflows/python-app.yml)

Наш проект представляет web приложение и TG бот для модификации фотографий, согласно описанию,  
также генерирует по полученной картинке музыку!  
Попробуйте, будет весело

Пример работы приложения  
![image](Img/example.png)

## :gem: Модели:

<p>fffiloni/img-to-music https://huggingface.co/spaces/fffiloni/img-to-music</p>
<p>mikonvergence/theaTRON https://huggingface.co/spaces/mikonvergence/theaTRON</p>

## :gem: Команда:  

:arrow_forward: Абдюшев Никита Юрьевич (РИМ-130906),  
:arrow_forward: Ефимов Алексей Александрович (РИМ-130907),  
:arrow_forward: Кулиев Эмир Шамсаддинович  (РИМ-130908).

## :gem: How to use Telegram bot

### для запуска бота вам понадобится токен

1. Найдите @botfather в Telegram
2. Начните разговор с BotFather, нажав кнопку «Start».
3. Введите /newbot и следуйте инструкциям, чтобы настроить нового бота. BotFather
предоставит вам токен, который вы будете использовать для аутентификации своего бота и предоставления ему доступа к API Telegram.

### Настраиваем окружение (библиотеки, переменные и.т.д)

1. Устанавите библиотеку pyTelegramBotAPI
```
pip install pyTelegramBotAPI
```
3. Откройте свой любимый редактор кода и создайте файл .env для хранения вашего токена, как показано ниже.
```
export BOT_TOKEN=your-bot-token-here
```
3. Можете запускать бот
```
python3 tg_bot.py
```

## TODO list REMOVE THIS

#### markdown
links https://gist.github.com/rxaviers/7360908  
https://www.markdownguide.org/basic-syntax/  
  
#### Задание:  
:white_check_mark:   1. Сформируйте команду из 3-4 человек.  
:white_check_mark:   2. Создайте репозиторий на GitHub, который будет использоваться для командной разработки приложения.  
:white_check_mark:   3. Изучите возможности готовых библиотек машинного обучения.  
:x:   4. Сформулируйте задачу, которую вы хотите решить с помощью машинного обучения.  
:x:   5. Реализуйте решение выбранной вами задачи в коде с использованием готовой библиотеки машинного обучения.  
:x:   6. Отправьте реализованное решение в репозиторий на GitHub.  
:x:   7. Оформите документацию на ваше решение в репозитории.  
:x:   8. Отправьте ссылку на созданный репозиторий GitHub на платформу для проверки.  

Рекомендуется использовать одну из следующих библиотек машинного обучения:  
Hugging Face (https://huggingface.co/),  
TensorFlow Hub (https://www.tensorflow.org/hub),  
PyTorch Hub (https://pytorch.org/hub/),  
Keras Applications (https://keras.io/api/applications/).  
  
Пример репозитория – https://github.com/sozykin/ml_sentiment  


