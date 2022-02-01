""""
Aplication of recent earthquake
Modularitation with Function
Modularitation with Package
"""
from EartquakeNow import extraction_data, viewdata

if __name__ == "__main__":
    print(("main app"))
    result = extraction_data()
    viewdata(result)