import requests

def check_website_status(url):
    """Check the status of a website and return the result."""
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            result = "Успішно"
        else:
            result = f"Помилка: {status_code}"
        
        return status_code, result
    except requests.exceptions.RequestException as e:
        return None, f"Помилка підключення: {str(e)}"

def main():
    url = "https://google.com"
    print(f"Перевірка сайту: {url}")
    
    status_code, result = check_website_status(url)
    
    if status_code:
        print(f"Статус-код: {status_code}")
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()