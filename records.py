class Logbook:
    def __init__(self):
        self.log = []
        self.total_post_count = 0
        self.ace_post_count = 0
        self.bad_bot_count = 0
        self.last_post_time = 0

    def add_message(self, message):
        self.log.append(message)

    def print(self):
        for message in self.log:
            print(message)
    def get_total_post_count(self):
        return self.total_post_count
    def get_ace_post_count(self):
        return self.ace_post_count
    def set_last_post_time(self, time):
        self.last_post_time = time
    def get_bad_bot_count(self):
        return self.bad_bot_count
    def increment_bad_bot_count(self):
        self.bad_bot_count += 1
    def add_post_to_data(self, is_ace_post):
        self.total_post_count += 1
        if(is_ace_post == 1):
            self.ace_post_count += 1
