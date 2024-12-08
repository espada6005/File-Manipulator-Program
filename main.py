import os
import sys

class Manipulate:

    commands = ["reserve", "copy", "duplicate-contents", "replace-stirng"]

    @staticmethod
    def manipulate(arguments):
        if not Manipulate.validate(arguments):
            return "Wrong arguments...!!"
        else:
            return Manipulate.execute(arguments)

    #validate
    @staticmethod
    def validate(arguments):
        if not Manipulate.is_valid_length(arguments):
            return False
        
        command = arguments[1]
        if not Manipulate.is_valid_command(command):
            return False
        
        if command == Manipulate.commands[0]:
            return Manipulate.is_valid_args_of_reserve(arguments)
        elif command == Manipulate.commands[1]:
            return Manipulate.is_valid_args_of_copy(arguments)
        elif command == Manipulate.commands[2]:
            return Manipulate.is_valid_args_of_duplicate(arguments)
        elif command == Manipulate.commands[3]:
            return Manipulate.is_valid_args_of_replace(arguments)
        else:
            return False

    @staticmethod
    def is_valid_length(arguments):
        length = len(arguments)
        return length == 4 or length == 5
    
    @staticmethod
    def is_valid_command(command):
        return command in Manipulate.commands

    @staticmethod
    def is_valid_args_of_reserve(arguments):
        return ManipulateHelper.file_exits(arguments[2]) and Manipulate.overwrite_confirm(arguments[3])
    
    @staticmethod
    def is_valid_args_of_copy(arguments):
        return ManipulateHelper.file_exits(arguments[2]) and Manipulate.overwrite_confirm(arguments[3])
    
    @staticmethod
    def is_valid_args_of_duplicate(arguments):
        return ManipulateHelper.file_exits(arguments[2]) and arguments[3].isnumeric() and int(arguments[3]) >= 0
    
    @staticmethod
    def is_valid_args_of_replace(arguments):
        return ManipulateHelper.file_exits(arguments[2]) and Manipulate.overwrite_confirm(arguments[4])
    
    @staticmethod
    def overwrite_confirm(path):
        allow_overwriting = 1

        if ManipulateHelper.file_exits(path):
            allow_overwriting = ManipulateHelper.confirm("ファイルはすでに存在しています。上書きしますか？(Y/N)：")
        
        while allow_overwriting == -1:
            allow_overwriting = ManipulateHelper.confirm("Y,N以外が入力されました。ファイルはすでに存在しています。上書きしますか？(Y/N)：")
        
        return bool(allow_overwriting)

    # Execute
    def execute(arguments):
        command = arguments[1]
        if command == Manipulate.commands[0]:
            return Manipulate.reverse(arguments[2], arguments[3])
        elif command == Manipulate.commands[1]:
            return Manipulate.copy(arguments[2], arguments[3])
        elif command == Manipulate.commands[2]:
            count = int(arguments[3])
            return Manipulate.duplicate(arguments[2], count)
        elif command == Manipulate.commands[3]:
            return Manipulate.replace(arguments[2], arguments[3], arguments[4])
        else:
            return "問題が発生しました"

    @staticmethod
    def reverse(inputPath, outputPath):
        print("ファイル読み込み")        
        with open(inputPath) as f:
            contents = f.read()
        print("読み込み完了")
    
        contents = contents[::-1]

        print("ファイル書き込み")
        with open(outputPath, 'w') as f:
            f.write(contents)
        print("書き込み完了")

        return "処理完了"
    
    @staticmethod
    def copy(inputPath, outputPath):
        print("ファイル読み込み")        
        with open(inputPath) as f:
            contents = f.read()
        print("読み込み完了")
    
        print("ファイル書き込み")
        with open(outputPath, 'w') as f:
            f.write(contents)
        print("書き込み完了")

        return "処理完了"
    
    @staticmethod
    def duplicate(inputPath, n):
        if n == 0:
            return "複製失敗"
        
        print("ファイル読み込み")
        with open(inputPath) as f:
            contents = f.read()
        print("読み込み完了")

        print("複製開始")
        with open(inputPath, 'a') as f:
            while n > 0:
                f.write(contents)
                n -= 1
        print("複製完了")
        
        return "処理完了"

    
    @staticmethod
    def replace(inputPath, needle, newstring):
        print("ファイル読み込み")
        with open(inputPath) as f:
            contents = f.read()
        print("読み込み完了")

        contents = contents.replace(needle, newstring)

        print("ファイル書き込み")
        with open(inputPath, 'wt') as f:
            f.write(contents)
        print("書き込み完了")

        return "処理完了"


# Helper
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
        
if __name__ == "__main__":
    print(Manipulate.manipulate(sys.argv))