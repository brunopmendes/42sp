import sys
from antigravity import geohash

def main():

    try:
        args = sys.argv
        if len(args) != 4:
            raise Exception('Number of arguments other than 4')
        
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = bytes(sys.argv[3], encoding='utf-8')

        geohash(latitude=latitude, longitude=longitude, datedow=datedow)
            
    except Exception as e:
        print(f'Exception: {e}')

if __name__ == '__main__':
    main()