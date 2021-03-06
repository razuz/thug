
import logging
log = logging.getLogger("Thug")

def CreateObject(self, _object, param = ''):
    import ActiveX

    log.ThugLogging.add_behavior_warn("[VsmIDE.DTE ActiveX] CreateObject (%s)" % (_object))
    log.ThugLogging.log_exploit_event(self._window.url,
                                      "VsmIDE.DTE ActiveX",
                                      "CreateObject",
                                      data = {
                                                "object": _object
                                             },
                                      forward = False)

    return ActiveX.ActiveX._ActiveXObject(self._window, _object)

