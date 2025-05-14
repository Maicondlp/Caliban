import re

class ErrorHandler:
    @staticmethod
    def is_valid_url(url):
        url_pattern = re.compile(
            r'^(https?://)([a-z0-9]+([-.][a-z0-9]+)*\.[a-z]{2,})(:[0-9]{1,5})?(/.*)?$', 
            re.IGNORECASE
        )
        return bool(re.match(url_pattern, url))
