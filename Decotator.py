def my_first_fun(func):
    def my_second_fun():
        print("exeute")
        func()
        print("done")
    return my_second_fun

def greeter():
    print("Hello my name is LaVance")

greeter = my_first_fun(greeter)

greeter()

# Decotator is use to pass a funtion into a other funtion to return the output of a third funtion