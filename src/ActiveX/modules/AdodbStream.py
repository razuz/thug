try:
    from io import StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

import logging
from Magic.Magic import Magic
log = logging.getLogger("Thug")

def open(self): #pylint:disable=redefined-builtin
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] open")
    self.fobject = StringIO()

def Write(self, s):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] Write")
    self.fobject.write(unicode(s))

def SaveToFile(self, filename, opt = 0):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] SaveToFile(%s, %s)" % (filename, opt, ))
    log.ThugLogging.log_exploit_event(self._window.url,
                                      "Adodb.Stream ActiveX",
                                      "SaveToFile",
                                      data = {
                                                "file": filename
                                             },
                                      forward = False)

    content = self.fobject.getvalue()
    mtype   = Magic(content).get_mime()

    log.ThugLogging.log_file(content, url = filename, sampletype = mtype)
    self._files[filename] = content

def LoadFromFile(self, filename):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] LoadFromFile(%s)" % (filename, ))
    if filename not in self._files:
        raise TypeError()

    self._current = filename

def ReadText(self, NumChars = -1):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] ReadText")

    if NumChars == -1:
        return self._files[self._current]

    return self._files[self._current][:NumChars - 1]

def WriteText(self, data, options = None):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] WriteText(%s)" % (data, ))

def Close(self):
    log.ThugLogging.add_behavior_warn("[Adodb.Stream ActiveX] Close")
    self.fobject.close()
