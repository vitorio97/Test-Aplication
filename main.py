""""
Aplication of recent earthquake
Modularitation with Function
Modularitation with Package
"""
import EartquakeNow

if __name__ == "__main__":
    print(("main app"))
    result = EartquakeNow.extraction_data()
    EartquakeNow.viewdata(result)