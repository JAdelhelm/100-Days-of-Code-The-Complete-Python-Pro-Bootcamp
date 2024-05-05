from flask import Flask
from random import randint
app = Flask(__name__)

def make_h1(function):
    def wrapper_function():
        """
        Changes the result of the originally function, then returns it.
        The wrapper_function will be called and the corresponding
        modified result will be returned.
        """
        result = function()
        result_modified = "<h1 style='text-align: center'>"+result+"</h1>"
        return result_modified
    
    return wrapper_function

    

@app.route("/")
@make_h1
def show_number():
    return  "Guess a number between 0 and 9 <br>" \
            "<img style='margin-top: 25px' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"



@app.route("/<int:guess_id>")
def guess_number(guess_id):
    gen_number = randint(0,9)
    if guess_id < gen_number:
        return "<h1 style=color:red>Too low, try again!</h1><br>" \
                "<img src='https://media3.giphy.com/media/cr9vIO7NsP5cY/giphy.gif?cid=ecf05e474ly45ttzqgmdzymkf5o9r8fjcjyly8q33yrkvk40&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif guess_id > gen_number:
        return "<h1 style=color:#8A2BE2>Too high, try again!</h1><br>" \
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWF2dGpjanA2NDhkNWVpMWxyaTBjaHp2cXN4Z3IwazdhOHpnNjk3aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OoD8xXGGQXbQlbiqzH/giphy.gif'>"
    else:
        return "<h1 style=color:#3CB371>You found me!</h1><br>" \
                "<img src='https://media2.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif?cid=ecf05e47n8tji608praafj14imzwjyttcwxk12kgjwn33puh&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"



if __name__ == "__main__":
    app.run(debug=True)

    