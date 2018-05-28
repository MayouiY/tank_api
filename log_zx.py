class Log_zx:
    def __init__(self):
        self.output = open('log_zx.txt', "w")
        self.output.close()

    def log(self,all_the_text):
        text = str(all_the_text)+"\n"
        self.output = open('log_zx.txt', "a")
        self.output.write(text)
        self.output.close()

log = Log_zx()



