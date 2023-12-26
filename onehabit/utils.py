class DevUtils:
    
    @staticmethod
    def assert_as_list(x):
        if not isinstance(x, list):
            x = [x]
        return x