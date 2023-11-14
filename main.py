from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
host_name = 'localhost' # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    '''
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    '''
    def do_GET(self):
        '''Метод для обработки входящих GET-запросов'''
        self.send_response(200) # Отправка кода ответа
        self.send_header('Content-type', 'application/json')
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes("{'message': 'OK'", "utf-8")) # Тело ответа


if __name__ == '__main__':
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((host_name, serverPort), MyServer)
    print('Server started http://%s:%s' % (host_name, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()