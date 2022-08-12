from os import system #just to change window title
import time #give a few seconds for the error reason
def main():
    system("title " + "Tasque Meowifier")
    #Make person choose what do they want
    print("What would you like to do?\n1.Meowify text\n2.Unmeowify text\n3.Unmeowify text from output.txt (for beginner linux users or really long meowified text)")
    option = int(input())
    if option == 1:
        print("Insert text below:")
        txt = input()
        #Turn everything into binary
        res = ''.join(format(ord(i), '08b') for i in txt)
        #Then meowify it
        meow = res.replace("0", "me").replace("1", "ow")
        print("Meowified text:" + meow)
        #Save to file for people running the exe
        file = open("output.txt", "w")
        file.write(meow)
    elif option == 2:
        print("Insert text below (If the text is from output.txt, open it and copy and paste into the console):")
        txt = input()
        try:
            #Turn meowified text back into binary
            meow = txt.replace("me", "0").replace("ow", "1").replace(" ", "") #incase someone adds a space accidentally between the text, crashing the program
            def binarytodecimal(binary):
                binary1 = binary
                decimal, i, n = 0, 0, 0
                while(binary != 0):
                    dec = binary % 10
                    decimal = decimal + dec * pow(2, i)
                    binary = binary//10
                    i += 1
                return(decimal)

            str_data = ''
            #Return to normal text
            for i in range(0, len(meow), 8):
                temp_data = int(meow[i:i + 8])
                decimal_data = binarytodecimal(temp_data)
                str_data = str_data + chr(decimal_data)
            print("Binary text: " + meow)
            print("Normal text: " + str_data)
            #Save to file for people running the exe
            file = open("translate.txt", "w")
            file.write(meow + "\n" + str_data)
            print("If text was not translated correctly, emojis may have been used")
        except Exception as exception:
            print("This isn't a meowified text. Full error:")
            print(exception)
            #Draw error without closing in the exe
            print("Feel free to close the program if you read it, otherwise it'll close in 10 seconds.")
            time.sleep(10)
    else:
        try:
            file = open("output.txt", "r")
            txt = file.read()
            #Turn meowified text back into binary
            meow = txt.replace("me", "0").replace("ow", "1").replace(" ", "") #incase someone adds a space accidentally between the text, crashing the program
            def binarytodecimal(binary):
                binary1 = binary
                decimal, i, n = 0, 0, 0
                while(binary != 0):
                    dec = binary % 10
                    decimal = decimal + dec * pow(2, i)
                    binary = binary//10
                    i += 1
                return(decimal)

            str_data = ''
            #Return to normal text
            for i in range(0, len(meow), 8):
                temp_data = int(meow[i:i + 8])
                decimal_data = binarytodecimal(temp_data)
                str_data = str_data + chr(decimal_data)
            print("Binary text: " + meow)
            print("Normal text: " + str_data)
            #Save to file for people running the exe
            file = open("translate.txt", "w")
            file.write(meow + "\n" + str_data)
            print("If text was not translated correctly, emojis may have been used")
        except Exception as exception:
            print("Either this file doesn't exist or something happened. Full error:")
            print(exception)
            #Draw error without closing in the exe
            print("Feel free to close the program if you read it, otherwise it'll close in 10 seconds.")
            time.sleep(10)


if __name__  == "__main__":
    main()
