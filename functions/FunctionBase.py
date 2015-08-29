
class FunctionBase(object):

    @classmethod
    def getName(self):
        return ''
    
    @classmethod
    def getControlNames(self):
        return [ '' ]
    
    @classmethod
    def isEdgeBase(self):
        return False
    
    @classmethod
    def canExport(self):
        return False

    def isSupportedVersion(self, version):
        return (self.minVersion <= version and version <= self.maxVersion)

    def prepare(self, canvasItemList):
        pass
    
    def getQuery(self, args):
        return ''
    
    def draw(self, rows, con, args, geomType, canvasItemList, mapCanvas):
        pass
    
    def __init__(self, ui):
        self.ui = ui
        self.minVersion = 2.0
        self.maxVersion = 2.99