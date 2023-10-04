
from    config      import  FILES, COLUMNS, ID_FMT, DLY_FMT
from    polars      import  col, from_pandas, read_csv
from    yfinance    import  Ticker
from    sys         import  argv
from    time        import  time


if __name__ == "__main__":

    t0      = time()
    mode    = argv[1]   if len(argv) > 1    else None
    header  = False     if mode == "init"   else True 

    for dfn in FILES:

        interval    = dfn[0]
        in_fn       = dfn[1]
        out_fn      = dfn[2]
        yf_ticker   = dfn[3]
        fmt         = ID_FMT if "d" not in interval else DLY_FMT

        if mode != "init":

            in_fn   = out_fn

        df          = read_csv(in_fn, has_header = header, new_columns = COLUMNS)
        tick        = Ticker(yf_ticker)
        hist        = from_pandas(
                        tick.history(period = "max", interval = interval),
                        include_index = True
                    )
        
        if hist.is_empty():

            # interval not supported or some other error

            continue

        hist_cols   = hist.columns[0:len(COLUMNS)]
        name_map    = {
                        hist_cols[i] : COLUMNS[i]
                        for i in range(len(hist_cols))    
                    }
        hist        = hist.rename(name_map).select(COLUMNS)
        hist        = hist.with_columns(hist[COLUMNS[0]].dt.strftime(fmt))
        last_ts     = df.item(-1, 0)
        new_recs    = hist.filter(col(COLUMNS[0]) > last_ts)

        '''
        print(interval)
        print(df.tail())
        print(hist.head())
        print(new_recs.head())
        '''

        df = df.vstack(new_recs)

        # print(df.tail())

        df.write_csv(file = out_fn)

    print(f"elapsed: {time() - t0:0.1f}")