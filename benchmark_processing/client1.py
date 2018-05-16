from uuid import uuid1 
import pickle, socket, sys, time
import matplotlib.pyplot as plt
import pdb

class Message(object):
    def __init__(self, src=1, dst=99, origin_coord=[10,20,30], type=1, data="nothing"):
        self.id = uuid1()
        self.src = src
        self.dst = dst
        self.origin_coord = origin_coord
        self.type = type
        self.data = data
        self.timestamp = time.time()
        

def start_client(server_address):
    mydict = dict()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for _ in range(1000):
        msg = Message()
        mydict[msg.id] = [msg.timestamp]
        b = pickle.dumps(msg)
        #pdb.set_trace()
        sock.sendto(b, server_address)
        d, server = sock.recvfrom(4096)
        d = pickle.loads(d)
        #pdb.set_trace()
        mydict[d.id].append(time.time())
    dffs = [t2-t1 for t1, t2 in mydict.values()]
    pdb.set_trace()
    plt.plot(dffs, linewidth=0.1)
    plt.show(dffs)
    
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        server_address = ("localhost", 10000)
    else:
        server_address = (sys.argv[1], int(sys.argv[2]))
    start_client(server_address)

    