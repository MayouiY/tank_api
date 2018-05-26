
from Start import *
import os
import sys
import socket
import json
import time


def main():
    print(sys.argv)
    if len(sys.argv) < 4:
        print("Usage: %s [TeamId] [ServerIp] [ServerPort]\n" % os.path.basename(sys.argv[0]))
        return -1
    team_id = int(sys.argv[1])
    server_ip = sys.argv[2]
    server_port = int(sys.argv[3])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(30)
    for _ in range(30):
        try:
            sock.connect((server_ip, server_port))
            time.sleep(1)
            break
        except socket.timeout:
            print("Wait server time out, exit ...")
            sock.close()
            return 1
        except Exception as ex:
            print("Socket connection:%s, retry ..." % ex)

    else:
        sock.close()
        print("Wait server time out, exit ...")
        return 1

    try:
        start_round(sock, team_id)
    finally:
        sock.close()


if __name__ == '__main__':
    sys.exit(main())
