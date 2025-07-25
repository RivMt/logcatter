from src.logcatter import Log

Log.setLevel(Log.VERBOSE)
Log.save("log.log")
Log.d(f"Current verbose={Log.is_verbose()}")
Log.d("This is DEBUG")
Log.i("This is INFO")
Log.w("This is WARNING")
Log.e("This is ERROR")
Log.e("This is ERROR with Exception", e=ValueError())
Log.e("This is ERROR with Exception, Stacktrace", e=ValueError(), s=True)
Log.f("This is CRITICAL")
Log.f("This is CRITICAL with Exception", e=ValueError())
Log.f("This is CRITICAL with Exception, Stacktrace", e=ValueError(), s=True)
Log.setLevel(Log.ERROR)
Log.e(f"Current verbose={Log.is_verbose()}")