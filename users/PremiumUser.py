from User import User

class PremiumUser(User):
    def __init__(self, name):
        parent_instance = super()
        parent_instance.__init__(name)
        
        self.is_premium = True