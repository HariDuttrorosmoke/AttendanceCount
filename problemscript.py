def main():
    userinput = input(str("Enter the file that you want to read: "))
    myfile = open(userinput)
    info_list = myfile.readlines() #this will be changed later depending on problem.
    whitespace_remover(info_list) # whitespace function call
    dateORatt(info_list)
    myfile.close()

def whitespace_remover(info_list):
    for element in info_list:
        if element == "\n":
            info_list.pop(info_list.index(element))
    #print(info_list)

def dateORatt(info_list):
    for i in range(0,len(info_list)):
        if i%2==0:
            number = []
            number = len(info_list[i+1].split())
            print("Total students attended on {date} are {numberatt}".format(date=info_list[i],numberatt=number))

main() #Main function call
