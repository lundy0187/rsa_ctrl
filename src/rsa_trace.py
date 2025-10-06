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
    # save trace to file
    #print('MMEM:SPEC:MEAS:STOR:TRAC1\"' + 'C:\\Users\\Public\\Documents\\' + params.FileName + '\"')
    rsa.write('MMEM:SPEC:MEAS:STOR:TRAC \"' + 'C:\\Users\\Public\\Documents\\' + params.FileName + '\"')
    print(rsa.query('MMEM:SPEC:MEAS:STOR:PLOT:DON?'))
    while not rsa.query('MMEM:SPEC:MEAS:STOR:PLOT:DON?'):
        time.sleep(2)
