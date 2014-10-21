from plugin_mods import UserModules

mod_class = UserModules()

def main_function():
    i = 1

    for name in mod_class.usr_modules:
        print("[{}] - {}".format(i, name))
        i+=1

    usr_choice = int(input("Select number: ")) - 1
    mod_class.usr_modules[list(mod_class.usr_modules.keys())[usr_choice]].exec_module()
