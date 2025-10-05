# initial parameters
runFile = 'cfg/runs.csv'
cmdDelay = 0.05
ipAddr = '172.16.152.131'
port = 4000 

if __name__ == "__main__":
    # import pandas and read in run sheet
    import pandas as pd
    params = pd.read_csv(runFile)

    # import keysight socketscpi library
    import sys
    sys.path.append('extern/socketscpi/socketscpi')
    from socketscpi import SocketInstrument

    # instantiate execution objects
    import src.rsa_trace as rsaObj
    rsa = SocketInstrument(ipAddr, port=port)

    # execute
    for paramsInd in range(0, len(params)):
        rsaObj.make_trace(rsa, params.iloc[paramsInd], cmdDelay)
