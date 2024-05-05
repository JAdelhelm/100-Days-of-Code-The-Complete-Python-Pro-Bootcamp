# %%
class UserLogin():
    def __init__(self, user_name, is_logged_in) -> None:
        self.is_logged_in = is_logged_in
        self.user_name = user_name


    def user_is_logged_in(function):
        def wrapper_function(*args, **kwargs):
            if args[0].is_logged_in == True:
                function(args[0])
        
        return wrapper_function

    @user_is_logged_in
    def post_blog(self):
        print(f"User {self.user_name} posts something!")





if __name__ == "__main__":
    user = UserLogin("JAdel", True)
    user.post_blog()
