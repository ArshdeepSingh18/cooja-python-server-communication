import socket

IPADDR = "fd00::1"
PORT = 5678

def create_socket(ipaddr: str, port: int):
    """Creates a new IPv6 UDP socket."""
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    # The below REUSEADDR option is selected, which allows python to use an IP address
    # already in use, by tunslip6.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the given ipaddr and port.
    s.bind((ipaddr, port))

    return s

def main():
    try:
        s = create_socket(IPADDR, PORT)

        count = 0;
        while True:
            # Extract information from incoming packets.
            data, address = s.recvfrom(1024)
            print(f"[PACKET:] {data.decode('ascii')} [IP:] {address[0]} [PORT:] {address[1]}")

            # Send back packets to the address.
            packet = f"Data packet {count}".encode("ascii")
            count += 1
            s.sendto(packet, address)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
