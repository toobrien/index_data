
COLUMNS = [ "datetime", "open", "high", "low", "close" ]
ID_FMT  = "%Y-%m-%d %H:%M:%S"
DLY_FMT = "%Y-%m-%d"
ROOT    = "."
FILES   = [
    ( "1d",     f"{ROOT}/SPX/SPX_full_1day.txt",    f"{ROOT}/SPX/SPX_daily.csv",    "^GSPC"   ),
    #( "1h",     f"{ROOT}/SPX/SPX_full_1hour.txt",   f"{ROOT}/SPX/SPX_1h.csv",       "^GSPC"   ),
    ( "1m",     f"{ROOT}/SPX/SPX_full_1min.txt",    f"{ROOT}/SPX/SPX_1m.csv",       "^GSPC"   ),
    #( "5m",     f"{ROOT}/SPX/SPX_full_5min.txt",    f"{ROOT}/SPX/SPX_5m.csv",       "^GSPC"   ),
    #( "30m",    f"{ROOT}/SPX/SPX_full_30min.txt",   f"{ROOT}/SPX/SPX_30m.csv",      "^GSPC"   )
]