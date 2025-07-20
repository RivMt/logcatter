from src.logcatter import Log

Log.setLevel(Log.VERBOSE)
with Log.print_log(s=True):
    for i in range(10):
        print(f"Index {i}")