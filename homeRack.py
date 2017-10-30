import time
import os

class Fact(object):  # {{{
    """
    Base class for all facts

    A `fact` is a basic unit of information collection in this script. This is a base class
    providing the common functions such as output formatting.
    """
    WHITE = '\033[1m'
    GREEN = '\033[1;32m'
    CYAN = '\033[0;96m'
    ORANGE = '\033[1;33m'
    RED = '\033[1;31m'
    RESET = '\033[0m'

    # Fact's severity
    NONE = 0  # no useful output
    INFO = 1
    WARN = 2
    CRIT = 3
    _severity = NONE
    _lines = []

    HEADER = None

    def _header(self, msg):
        self._severity = max(self._severity, self.INFO)
        return self.WHITE + msg + self.RESET

    def _ok(self, msg):
        self._severity = max(self._severity, self.INFO)
        return self.GREEN + msg + self.RESET

    def _warning(self, msg):
        self._severity = max(self._severity, self.WARN)
        return self.ORANGE + msg + self.RESET

    def _critical(self, msg):
        self._severity = max(self._severity, self.CRIT)
        return self.RED + msg + self.RESET

    def multiline(self, minseverity=INFO, limit=None):
        if self._severity < minseverity or len(self._lines) == 0:
            return []
        lines = self._lines
        if limit and len(lines) > limit:
            lines = ["...(%dx more)..." % (len(lines)-limit)] + lines[-limit:]
        if self.HEADER:
            lines = [self.WHITE + self.HEADER + ':' + self.RESET] + lines
        return lines

class homeRack(Fact):
    """
    Information about /home/rack disk usage
    """
    def __init__(self):
        self.check_dir = '/home/rack'
        self.total_size = 0

        func_start = time.time()

        for dirpath, _, filenames in os.walk(self.check_dir):
            func_check_time = time.time()
            func_time = func_check_time - func_start
            if func_time >= 0.25:
                break
            for f in filenames:
                fpath = os.path.join(dirpath, f)
                self.total_size += os.path.getsize(fpath)

        func_finish = time.time()
        func_time = func_finish - func_start

        self.total_size = float( (self.total_size / float(1024)) / float(1024) )
        self.total_size = round(float(self.total_size / float(1024)), 2)


        if func_time >= 0.25:
            _lines = '/home/rack summary exceeded %s0.25s%s. Size' \
                ' calculated in this time: %s GB+, please investigate' % (self.RED, self.RESET, (str(self.total_size)))
        elif self.total_size >= 1:
            _lines = '/home/rack large: %s GB+ - time taken: %s' % (
                 (str(self.total_size)  ), str(func_time))
        else:
            _lines = ['/home/rack timetaken: ' + (str(func_time))]

        print _lines

homeRack()
