import os
import platform
import time

def ping_host(host):
    """
    Mando un pacchetto ICMP all'host che ritorna true se risponde false se non risponde
  
    """
    if platform.system().lower() == 'windows':
        ping_cmd = f"ping -n 1 {host}"
    else:
        ping_cmd = f"ping -c 1 {host}"
    response = os.system(ping_cmd)
    return response == 0

def monitor_hosts(hosts):
    """
    Monitoraggio disponibilità degli host e stampo il loro stato

    """
    while True:
        for host in hosts:
            if ping_host(host):
                print(f"{host}: Online")
            else:
                print(f"{host}: Offline")
        time.sleep(1)  # rifaccio il check dopo 1 sec.
        
def main():
    """
    Faccio il get degli host da monitorare e monitoro

    """
    hosts = input("Immettere la lista degli host da monitorare dividendo per virgola: ")
    hosts = [host.strip() for host in hosts.split(",")]
    print("Monitoraggio hosts:")
    for host in hosts:
        print(f"  - {host}")
    monitor_hosts(hosts)

try:
    main()
except KeyboardInterrupt:
    print("Monitoraggio stoppato da user") #usando ctrl + c
except Exception as e:
    print(f"Errore: {e}")