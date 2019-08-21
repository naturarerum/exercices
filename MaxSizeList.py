class MaxSizeList(object):
    def __init__(self, long_max):
        """constructeur"""
        self.long = long_max
        self.list_attr = []

    def get_max_size(self):
        print("maxSize :")
        return self.long
    #
    def get_list(self):
        return self.list_attr

    def set_attrs(self, listattrs):
        pass



