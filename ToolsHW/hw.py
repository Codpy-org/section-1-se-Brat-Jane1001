import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
 
 
ERROR_COUNT = 0

def input_math():
    global ERROR_COUNT
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                opEn_vIdeo()
            
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                opEn_vIdeo() 
    except:
        ERROR_COUNT -= 1
        pass 

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
input_math()
