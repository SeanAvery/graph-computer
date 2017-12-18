from time import sleep

class User():
    def user_daemon(self):
        sleep(2)
        print('sending transaction')
        return self.user_daemon()

user = User()
user.user_daemon()
