from os import system #just to change window title
def main():
    system("title " + "Text Meowifier")
    #Make person choose what do they want
    print("What would you like to do?\n1.Meowify text\n2.Unmeowify text")
    option = int(input())
    
    if option == 1:
        print("Insert text below:")
        txt = input()
        #Turn everything into binary
        res = ''.join(format(ord(i), '08b') for i in txt)
        #Then meowify it
        meow = res.replace("0", "me").replace("1", "ow")
        print(meow)
    else:
        print("Insert text below:")
        txt = input()
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

        str_data = ' '
        #Return to normal text
        for i in range(0, len(meow), 8):
            temp_data = int(meow[i:i + 8])
            decimal_data = binarytodecimal(temp_data)
            str_data = str_data + chr(decimal_data)
        print("Binary text: " + meow)
        print("Normal text: " + str_data)
        print("If text was not translated correctly, emojis may have been used")

if __name__  == "__main__":
    main()
