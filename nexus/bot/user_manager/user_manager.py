import time


class UserManager:
    def __init__(self):
        self.last_widget = {}
        self.search_times = {}
        self.search_ban_times = {}

    def add_search_time(self, user_id: str, search_time: float):
        current_time = time.time()
        search_times = self.search_times.get(user_id, [])
        search_times.append(search_time)
        counter = 0

        for i in reversed(search_times):
            if i > current_time - 10:
                counter = counter + 1
                if counter > 5:
                    self.search_ban_times[user_id] = current_time + int(60)
                    del self.search_times[user_id]
                    return
            else:
                if counter == 1:
                    del self.search_times[user_id]
                    return

        if len(search_times) > 20:
            self.search_ban_times[user_id] = current_time + int(120)
            del self.search_times[user_id]
            return

        self.search_times[user_id] = search_times

    def check_search_ban_timeout(self, user_id: str):
        ban_time = self.search_ban_times.get(user_id)
        if ban_time:
            timeout = int(ban_time - time.time())
            if timeout > 0:
                return timeout
            del self.search_ban_times[user_id]
