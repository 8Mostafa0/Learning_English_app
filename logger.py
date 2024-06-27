import datetime
class logger():
    def __init__(self) -> None:
        self.file = "Logs.txt"
        self.check_files()
    
    def get_time(self):
        return datetime.datetime.now().time()

    def check_files(self):
        with open(self.file,"w") as file: 
            file.write(f"{self.get_time()} # Log File Created\n")

    def log(self,text):
        with open(self.file,"a") as file:
            file.write(f"{self.get_time()} # {text}\n")
