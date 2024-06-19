class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.entry_number = 1
    
    def add_entry(self, entry_text):
        with open(self.filename, 'a') as file:
            # Create the log entry with the number in square brackets
            log_entry = "[{}] {}".format(str(self.entry_number).rjust(5), entry_text)
            file.write(log_entry + "\n")
            self.entry_number += 1

# Test script
logger = Logger('log.txt')
logger.add_entry('First entry.')
logger.add_entry('Second entry.')
logger.add_entry('The PDS MEP is running!')
