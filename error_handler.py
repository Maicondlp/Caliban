import re

class ErrorHandler:
    @staticmethod
    def is_valid_url(url):
        url_pattern = re.compile(
            r'^(https?://)([a-z0-9]+([-.][a-z0-9]+)*\.[a-z]{2,})(:[0-9]{1,5})?(/.*)?$', 
            re.IGNORECASE
        )
        return bool(re.match(url_pattern, url))

# Exemplo de uso
print(ErrorHandler.is_valid_url("https://www.example.com"))  # True
print(ErrorHandler.is_valid_url("http://example.com"))  # True
print(ErrorHandler.is_valid_url("example.com"))  # False (sem o protocolo)
print(ErrorHandler.is_valid_url("ftp://example.com"))  # False (protocolo não suportado)