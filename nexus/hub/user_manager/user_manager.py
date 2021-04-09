class UserManager:
    def __init__(self):
        self.last_widget = {}
        self.tasks = set()
        self.limits = {}

    def add_task(self, user_id, id):
        self.tasks.add((user_id, id))
        self.limits[user_id] = self.limits.get(user_id, 0) + 1

    def remove_task(self, user_id, id):
        try:
            self.tasks.remove((user_id, id))
            self.limits[user_id] = self.limits.get(user_id, 1) - 1
        except ValueError:
            pass

    def has_task(self, user_id, id):
        return (user_id, id) in self.tasks

    def hit_limits(self, user_id):
        return self.limits.get(user_id, 0) >= 3
