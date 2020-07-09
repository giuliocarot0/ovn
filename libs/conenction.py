class Connection(object):
    def __init__(self, inp, output, pwr):
        self._input = inp
        self._output = output
        self._signal_power = pwr
        self._latency = 0.0
        self._snr = 0.0

    @property
    def input_node(self):
        return self._input

    @property
    def output_node(self):
        return self._output

    @property
    def signal_power(self):
        return self._signal_power

    @signal_power.setter
    def signal_power(self, signal_pwr):
        self._signal_power = signal_pwr

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def latency(self, latency):
        self._latency = latency

    @property
    def snr(self):
        return self._snr

    @snr.setter
    def snr(self, snr):
        self._snr = snr

