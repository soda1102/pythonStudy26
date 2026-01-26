class Session:
    login_member = None
    cart = []

    @classmethod
    def login(cls, member):
        cls.login_member = member
        cls.cart = []

    @classmethod
    def logout(cls):
        cls.login_member = None
        cls.cart = []

    @classmethod
    def is_login(cls):
        return cls.login_member is not None

    @classmethod
    def is_admin(cls):
        return cls.login() and cls.login_member.is_admin()

    @classmethod
    def is_manager(cls):
        return cls.login() and cls.login_member.is_manager()