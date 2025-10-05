import time

def make_trace(rsa, params, cmdDelay=0.05):
    """
    """
    # reset
    rsa.write('*RST', delay=cmdDelay)
    # set spec window
    rsa.write('SENS:SPEC:MEAS:FREQ:CENT ' + str(params.CentFreq_MHz) + ' MHz', delay=cmdDelay)
    rsa.write('SENS:SPEC:MEAS:FREQ:SPAN ' + str(params.Span_MHz) + ' MHz', delay=cmdDelay)
    # set spec trace settings
    rsa.write('SENS:SPEC:MEAS:BAND:RES ' + str(params.Rbw_kHz) + ' kHz', delay=cmdDelay)
    rsa.write('SENS:SPEC:MEAS:BAND:VID ' + str(params.Vbw_Hz) + ' Hz', delay=cmdDelay)
    rsa.write('SENS:SPEC:MEAS:POIN:COUN P' + str(params.SwpPts), delay=cmdDelay)
    rsa.write('TRAC:SPEC:MEAS:DET ' + params.Mode, delay=cmdDelay)
    rsa.write('TRAC:SPEC:MEAS:FUNC ' + params.Trace, delay=cmdDelay)
    # extract sweep time and build trace
    time.sleep(2)
