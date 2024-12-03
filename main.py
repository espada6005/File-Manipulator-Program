import os
import sys

class Manipulate:

    commands = ["reserve", "copy", "duplicate-contents", "replace-stirng"]

    @staticmethod
    def is_valid_length(arguments):
        length = len(arguments)
        return length == 4 or length == 5
    
    @staticmethod
    def is_valid_Command(command):
        return command in Manipulate.commands

    @staticmethod
    def is_valid_args_of_reserve(arguments):
        return ManipulateHelper.file_exits(arguments[2])
    
    @staticmethod
    def overwrite_confirm(path):
        allow_overwriting = 1

        if ManipulateHelper.file_exits(path):
            allow_overwriting = ManipulateHelper.confirm("ファイルはすでに存在しています。上書きしますか？(Y/N)：")
        
        while allow_overwriting == -1:
            allow_overwriting = ManipulateHelper.confirm("Y,N以外が入力されました。ファイルはすでに存在しています。上書きしますか？(Y/N)：")
        
        return bool(allow_overwriting)


class ManipulateHelper:

    @staticmethod
    def file_exits(path):
        return os.path.isfile(path)
    
    @staticmethod
    def confirm(question):
        answer = input(question)
        if answer == "y" or answer == "Y":
            return 1
        elif answer == "n" or answer == "N":
            return 0
        else:
            return -1
        