from zojax.resourcepackage.library import includes


class CrosspostingHeaders(object):
    
    def isAvailable(self):
        return 'zojax-crossposing' in includes.libraries
        