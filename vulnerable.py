# vulnerable.py
import os

def insecure_function(user_input):
    # コマンドインジェクションの脆弱性
    os.system("echo " + user_input)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_function(user_input)


# secret.txt
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLExx
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYxx
PASSWORD=cVPzhqptxrxsuqRSNwEUjfF7WCz5QVHLmn47VX2Q
PASSWORD=cVPzhqptxrxsuqRSNwEUjfF7WCz5QVHLmn47VX3Q
PASSWORD=cVPzhqptxrxsuqRSNwEUjfF7WCz5QVHLmn47VX4Q
