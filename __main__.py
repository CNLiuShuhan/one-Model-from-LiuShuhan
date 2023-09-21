#!/usr/bin/env python3
import runpy
try :
    it=runpy.run_path("./Center.pyc",run_name="__main__")
    if it == SystemExit:pass
    else:print('error :',it)
except SyntaxError as e:
    if str(e)=='source code string cannot contain null bytes':
        print('error code:0[out]c')
    else:
        print('error code:1[out]a')
except FileNotFoundError:
    print('error code:1[out]b,you can try to runing the rapairs.')
except RuntimeError:
    print('error code:0[out]a')
except MemoryError:
    print('error code:0[out]b')
