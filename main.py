""""
Aplication of recent earthquake
Modularitation with Function
"""


def extraction_data():
    """
    Date: 27 Januari 2022, 04:26:12 WIB
    Magnitude: 4.1
    Depth: 10 km
    Location: 2.73 LS - 121.99 BT
    Description: Pusat gempa berada di darat 6 km selatan Kab.Morowali
    Dirasakan (Skala MMI): II-III Bahodopi
    :return:
    """
    res = dict()
    res['date'] = '27 Januari 2022'
    res['time'] = '04:26:12 WIB'
    res['magn'] = '4.1'
    res['depth'] = '10 km'
    res['location'] = {'ls': 2.73, 'bt': 121.99}
    res['source'] = 'Pusat gempa berada di darat 6 km selatan Kab.Morowali'

    return res



def viewdata(result):
    print('Recent Earthquake')
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magn']}")
    print(f"Depth: {result['depth']}")
    print(f"Location: LS= {result['location']['ls']}, BT={result['location']['bt']} ")
    print(f"Source: {result['source']}")


if __name__ == "__main__":
    print(("main app"))
    result = extraction_data()
    viewdata(result)