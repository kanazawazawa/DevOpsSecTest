# vulnerable.py
import os

def insecure_function(user_input):
    # コマンドインジェクションの脆弱性
    os.system("echo " + user_input)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_function(user_input)

