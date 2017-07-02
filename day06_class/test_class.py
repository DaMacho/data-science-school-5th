class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print '{} sleep'.format(self.name)

    def work(self):
        print 'work'
