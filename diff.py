import requests

def solve_differential_equation_with_wolfram_alpha(query, api_key):
    """
    Использует API Wolfram Alpha для решения дифференциальных уравнений.
    :param query: строка с запросом для Wolfram Alpha.
    :param api_key: ваш API ключ от Wolfram Alpha.
    :return: Ответ от Wolfram Alpha.
    """
    base_url = "http://api.wolframalpha.com/v2/query"
    
    params = {
        "input": query,  # Ваш запрос для решения уравнения
        "format": "plaintext",  # Формат ответа (текст)
        "output": "JSON",  # Формат для получения данных
        "appid": api_key  # Ваш API ключ
    }
    
    try:
        # Отправляем запрос к API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Если возникла ошибка, выбрасывает исключение
        
        # Получаем данные в формате JSON
        data = response.json()
        
        # Проверка наличия результатов
        if "queryresult" in data and data["queryresult"]["success"]:
            pods = data["queryresult"]["pods"]
            for pod in pods:
                # Печатаем информацию из ответа
                if "subpods" in pod:
                    for subpod in pod["subpods"]:
                        print(subpod["plaintext"])
        else:
            print("Ошибка в запросе или нет решения.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")

# Пример использования
if __name__ == "__main__":
    query = "solve x*dx = y*dy"  # Пример дифференциального уравнения
    api_key = "ваш_API_ключ_от_Wolfram_Alpha"
    
    solve_differential_equation_with_wolfram_alpha(query, api_key)