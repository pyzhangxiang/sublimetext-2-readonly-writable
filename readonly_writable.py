# based on "Toggle Read-Only" (https://github.com/reflog/toggle-readonly)

import sublime, sublime_plugin, os, stat

class SetReadonlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        myFile = self.view.file_name()
        fileAtt = os.stat(myFile)[0]
        myPlatform = os.name

        print "Making " + myFile + " readonly"
        if (myPlatform == 'nt'):
            os.chmod(myFile, not stat.S_IWRITE)
        else:
            os.chflags(myFile, not stat.UF_IMMUTABLE)

    def is_enabled(self):
        print "is_enabled"
        if not self.view.file_name() or len(self.view.file_name()) <= 0:
            return False

        myFile = self.view.file_name()
        fileAtt = os.stat(myFile)[0]
        myPlatform = os.name

        if (myPlatform == 'nt'):
            if fileAtt & stat.S_IWRITE:
                return True
            else:
                return False
        else:
            if fileAtt & stat.UF_IMMUTABLE:
                return True
            else:
                return False


    def is_visible(self):
        return True


class SetWritableCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        myFile = self.view.file_name()
        fileAtt = os.stat(myFile)[0]
        myPlatform = os.name

        print "Making " + myFile + " writable"
        if (myPlatform == 'nt'):
            os.chmod(myFile, stat.S_IWRITE)
        else:
            os.chflags(myFile, stat.UF_IMMUTABLE)

    def is_enabled(self):
        if not self.view.file_name() or len(self.view.file_name()) <= 0:
            return False

        myFile = self.view.file_name()
        fileAtt = os.stat(myFile)[0]
        myPlatform = os.name

        if (myPlatform == 'nt'):
            if not (fileAtt & stat.S_IWRITE):
                return True
            else:
                return False
        else:
            if not (fileAtt & stat.UF_IMMUTABLE):
                return True
            else:
                return False

