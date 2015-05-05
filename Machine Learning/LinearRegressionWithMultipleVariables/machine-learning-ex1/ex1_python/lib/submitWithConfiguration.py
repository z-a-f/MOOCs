
class Config(object):
    def __init__(self, assignmentSlug = str(), itemName = str(), partArrays = {}):
        self.assignmentSlug = assignmentSlug
        self.itemName = itemName
        self.partArrays = partArrays
    def show(self):
        print "------------------------------------------------"
        print "Assignment Slug: %s" % self.assignmentSlug
        print "Item Name: %s" % self.itemName
        print "Part Arrays: ",
        print self.partArrays
