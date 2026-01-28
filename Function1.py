#this program prompts the user for their name and then greets them 


def main():
    #output greeting
    name = input("What is your name? ")
    hello(name)

    #output without passing the expected arguments
    hello()

def hello(to=''):
    print("Hello," , to)

#output greeting
name = input("What is your name? ")
hello(name)

#output without passing the expected arguments
hello()

main()
