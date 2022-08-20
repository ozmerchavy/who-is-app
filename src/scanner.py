import subprocess
from datetime import datetime
from os import walk
import os.path
from pathlib import Path
import json

"""
applies nmap in a loop, and writes results to files.
"""

ipconfig = subprocess.check_output(['ipconfig'], shell=True)
gatewayIP = str(ipconfig.split(b'Default Gateway')[-1], 'utf-8').replace(' .', '').replace(":", '').strip()

previous_data = []


def num_stuff_in_folder(dirname):
    filenames = next(walk(dirname), (None, None, []))[2]
    return len(filenames)

def today():
    return datetime.today().strftime('%Y-%m-%d')

def get_hostnames():
    import nmap
    print("Starting to Scan")
    scanner = nmap.PortScanner()
    scannedData = scanner.scan(gatewayIP+'/24', arguments ='sP')
    return scannedData['scan']


def lists_diff(current, earlier):
    return {
        "added": set(current) - set(earlier),
        "removed": set(earlier) - set(current)
    }


def read_names_json():
    try: 
        with open(f'{os.path.dirname(__file__)}/../names.json', 'r') as file:
            names = json.loads(file.read())
    except: 
        names = {}
    return names


def fetch_and_create_json(first_time):
    global previous_data

    list_ips = list(get_hostnames().keys())
    print("Completed a Scan")
    
    names = read_names_json()

    def name_of(ip):
        return f'({names[ip]})' if ip in names else '(unknown)'

    dirname = f'{os.path.dirname(__file__)}/../logs/{today()}'
    Path(dirname).mkdir(parents=True, exist_ok=True)  # make sure today's dir exists

    timestamp = datetime.now().strftime("%H:%M")

    with open(f'{dirname}/{num_stuff_in_folder(dirname)}.json', 'w') as file:
        json.dump({
                "at": timestamp,
                "online": {ip: name_of(ip) for ip in list_ips}
            },
            file, indent=2)
    
    diffs = lists_diff(list_ips, previous_data)
    
    with open(f'{os.path.dirname(__file__)}/../logs/delta-history.txt', "w" if first_time else "a") as file:
        file.write(timestamp + '\n')
        for info in ('added', 'removed'):
            for ip in diffs[info]:
                file.write(f'<span class="{info}">{ip} {name_of(ip)}</span>\n')
        file.write('\n')

    with open(f'{os.path.dirname(__file__)}/../logs/who-is-online.txt', 'w') as file:
        for ip in list_ips:
            file.write(f"{ip} {name_of(ip)}\n")
        
    previous_data = list_ips


def start_scanning():
    with open(f'{os.path.dirname(__file__)}/../logs/delta-history.txt', 'w') as file:
        file.write('')

    with open(f'{os.path.dirname(__file__)}/../logs/who-is-online.txt', 'w') as file:
        file.write('')
    
    fetch_and_create_json(first_time=True)
    while True:
        fetch_and_create_json(first_time=False)


if __name__ == '__main__':
    start_scanning()

 