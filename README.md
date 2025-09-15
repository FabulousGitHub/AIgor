<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIgor - Многофункциональный Telegram бот</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            padding: 40px 20px;
            border-bottom: 1px solid #30363d;
            margin-bottom: 40px;
        }
        
        h1 {
            font-size: 2.8rem;
            color: #58a6ff;
            margin-bottom: 15px;
        }
        
        .tagline {
            font-size: 1.4rem;
            color: #8b949e;
            margin-bottom: 20px;
        }
        
        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
        }
        
        .badge {
            display: inline-block;
            padding: 6px 12px;
            background-color: #21262d;
            border: 1px solid #30363d;
            border-radius: 6px;
            font-size: 0.9rem;
            color: #c9d1d9;
            text-decoration: none;
        }
        
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }
        
        @media (max-width: 768px) {
            .container {
                grid-template-columns: 1fr;
            }
        }
        
        .section {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 30px;
        }
        
        h2 {
            color: #58a6ff;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #30363d;
        }
        
        h3 {
            color: #f78166;
            margin: 15px 0 10px;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        
        .feature {
            background-color: #21262d;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #30363d;
        }
        
        .architecture {
            grid-column: 1 / -1;
        }
        
        .architecture-img {
            width: 100%;
            border-radius: 8px;
            border: 1px solid #30363d;
            margin: 20px 0;
        }
        
        .architecture-steps {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin: 20px 0;
        }
        
        .step {
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }
        
        .step-number {
            background-color: #58a6ff;
            color: #0d1117;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            flex-shrink: 0;
        }
        
        .step-content {
            flex: 1;
        }
        
        .api-badge {
            display: inline-block;
            padding: 3px 8px;
            background-color: #30363d;
            border-radius: 4px;
            font-size: 0.8rem;
            margin: 5px 5px 5px 0;
        }
        
        .code-block {
            background-color: #21262d;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
            margin: 15px 0;
        }
        
        code {
            font-family: 'Consolas', monospace;
            color: #d2a8ff;
        }
        
        .highlight {
            color: #ff7b72;
        }
        
        .comment {
            color: #8b949e;
        }
        
        footer {
            text-align: center;
            padding: 30px;
            border-top: 1px solid #30363d;
            margin-top: 40px;
            color: #8b949e;
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #238636;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
            margin: 10px 5px;
            transition: background-color 0.2s;
        }
        
        .btn:hover {
            background-color: #2ea043;
        }
        
        .btn-secondary {
            background-color: #21262d;
            border: 1px solid #30363d;
        }
        
        .btn-secondary:hover {
            background-color: #30363d;
        }
    </style>
</head>
<body>
    <header>
        <h1>AIgor</h1>
        <p class="tagline">Многофункциональный Telegram бот с мультиформатным вводом и выводом</p>
        
        <div class="badges">
            <span class="badge">Python</span>
            <span class="badge">Telegram Bot API</span>
            <span class="badge">Gemini AI</span>
            <span class="badge">Kadinsky</span>
            <span class="badge">OpenStreetMap</span>
        </div>
        
        <div>
            <a href="#" class="btn">Установить</a>
            <a href="#" class="btn btn-secondary">Документация</a>
        </div>
    </header>
    
    <div class="container">
        <div class="section">
            <h2>Возможности</h2>
            <div class="features-grid">
                <div class="feature">
                    <h3>📝 Генерация текста</h3>
                    <p>Мощная генерация текста с использованием модели Gemini</p>
                </div>
                <div class="feature">
                    <h3>🖼️ Генерация изображений</h3>
                    <p>Создание уникальных изображений по запросу с помощью Kandinsky</p>
                </div>
                <div class="feature">
                    <h3>🔊 Преобразование текста в речь</h3>
                    <p>Генерация аудио из текста с использованием Edge TTS</p>
                </div>
                <div class="feature">
                    <h3>🌐 Поиск в интернете</h3>
                    <p>Поиск актуальной информации через Google Search API</p>
                </div>
                <div class="feature">
                    <h3>🗺️ Поиск на картах</h3>
                    <p>Получение географических данных через OpenStreetMap</p>
                </div>
                <div class="feature">
                    <h3>⏰ Заметки с напоминаниями</h3>
                    <p>Создание и управление заметками с функцией напоминаний</p>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>Быстрый старт</h2>
            <h3>Установка</h3>
            <div class="code-block">
                <code>
                    <span class="comment"># Клонируйте репозиторий</span><br>
                    git clone https://github.com/FabulousGitHub/ai-bot.git<br>
                    cd ai-bot<br><br>
                    
                    <span class="comment"># Установите зависимости</span><br>
                    pip install -r requirements.txt<br><br>
                    
                    <span class="comment"># Настройте конфигурацию</span><br>
                    cp config.example.py config.py<br>
                    <span class="comment"># Отредактируйте config.py, добавив ваши API-ключи</span>
                </code>
            </div>
            
            <h3>Запуск</h3>
            <div class="code-block">
                <code>
                    <span class="comment"># Запустите бота</span><br>
                    python main.py
                </code>
            </div>
            
            <h3>Настройка окружения</h3>
            <p>Перед запуском необходимо получить и добавить в config.py:</p>
            <ul>
                <li>Telegram Bot Token от <a href="https://t.me/BotFather" style="color: #58a6ff;">@BotFather</a></li>
                <li>API ключ для Gemini</li>
                <li>API ключ для Google Search</li>
                <li>Другие необходимые ключи доступа</li>
            </ul>
        </div>
        
        <div class="section architecture">
            <h2>Архитектура системы</h2>
            <img src="https://github.com/user-attachments/assets/48e28e76-300a-45b8-8d12-1987c4e52bad" alt="Архитектура бота" class="architecture-img">
            
            <div class="architecture-steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Пользовательский запрос</h3>
                        <p>Пользователь отправляет запрос через Telegram API, который поступает в Telegram BOT</p>
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Определение команды</h3>
                        <p>Запрос анализируется моделью Gemini flash 1.5 8b для определения команды</p>
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Маршрутизация к API</h3>
                        <p>В зависимости от команды, бот обращается к соответствующему API:</p>
                        <div>
                            <span class="api-badge">Gemini flash 1.5</span>
                            <span class="api-badge">Kadinsky</span>
                            <span class="api-badge">OpenStreetMap</span>
                            <span class="api-badge">Google Search API</span>
                            <span class="api-badge">Edge TTS</span>
                        </div>
                    </div>
                </div>
                
                <div class="step">
                    <div class="step-number">4</div>
                    <div class="step-content">
                        <h3>Формирование ответа</h3>
                        <p>Бот получает ответ от API, формирует итоговый ответ и отправляет пользователю</p>
                    </div>
                </div>
            </div>
            
            <p>Архитектура бота демонстрирует эффективное использование множества сервисов для обеспечения широкого спектра функциональности, позволяя обрабатывать сложные и многогранные запросы.</p>
        </div>
    </div>
    
    <footer>
        <p>© 2023 FabulousGitHub - AIgor Telegram Bot</p>
        <p>Лицензия: MIT</p>
    </footer>
</body>
</html>
