import requests
import urllib3
from colorama import Fore, Style, init
from error_handler import ErrorHandler

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebScan:
    def verificaCabecalhosHTTP(self):
        try:
            response = requests.get(self.url, verify=False)

            for chave, valor in response.headers.items():
                print(f"{Fore.BLUE + chave} : {Fore.RESET + valor}")
            
            print(f"{Fore.LIGHTGREEN_EX}------------------------------------------------------------------------")

        except requests.exceptions.RequestException as e:
            print("*** Houve um problema na requisição")

    def verificaArquivoRobots(self):
        
        try:
            response = requests.get(self.url + "/robots.txt", verify=False)
            if response.status_code == 200:
                print(f"{Fore.BLUE}ROBOTS: {Fore.RESET}Arquivo robots.txt encontrado.")
            else:
                print(f"{Fore.BLUE}ROBOTS: {Fore.RESET}-------------")
        except requests.exceptions.RequestException as e:
            print("*** Houve um problema na requisição")



    def __init__(self,url):

        if not ErrorHandler.is_valid_url(url):
            print("Digite uma URl válida seguindo o padrão: [http[s]://example.com]")
        
        self.url = url

        
        self.verificaCabecalhosHTTP()
        self.verificaArquivoRobots()
    

