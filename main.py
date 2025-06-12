
from flask import request, render_template, Flask

app = Flask(__name__, template_folder='templates')  
  
@app.route("/")  
def web():  
    return render_template('index.html')  

@app.route('/check_join')
def check_join():
    # Получаем параметр hash из URL
    contest_hash = request.args.get('hash')
    
    # Проверяем валидность хэша (добавьте свою логику проверки)
    if not contest_hash or not is_valid_hash(contest_hash):
        return render_template('error.html', message="Неверный хэш конкурса"), 400
    
    # Получаем данные пользователя из Telegram WebApp
    init_data = request.args.get('tgWebAppData')
    user_data = parse_telegram_data(init_data) if init_data else None
    
    # Обработка участия в конкурсе
    return process_contest_participation(contest_hash, user_data)

def is_valid_hash(contest_hash: str) -> bool:
    """Проверяет валидность хэша конкурса"""
    # Ваша логика проверки хэша
    return len(contest_hash) == 12  # Пример простой проверки

def parse_telegram_data(init_data: str) -> dict:
    """Парсит данные пользователя из Telegram WebApp"""
    from urllib.parse import parse_qs
    parsed = parse_qs(init_data)
    
    return {
        'id': int(parsed.get('user', {}).get('id', [0])[0]),
        'first_name': parsed.get('user', {}).get('first_name', [''])[0],
        'last_name': parsed.get('user', {}).get('last_name', [''])[0],
        'username': parsed.get('user', {}).get('username', [''])[0],
    }

def process_contest_participation(contest_hash: str, user_data: dict = None):
    """Обрабатывает участие в конкурсе"""
    # Ваша бизнес-логика обработки участия hahaha
    
    if user_data:
        # Если есть данные пользователя (открыто через Mini App)
        return render_template('contest.html',
                            contest_hash=contest_hash,
                            user=user_data)
  
if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')  