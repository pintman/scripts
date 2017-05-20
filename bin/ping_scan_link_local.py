import multiprocessing
import subprocess
import os

# inspired by http://stackoverflow.com/questions/21225464/fast-ping-sweep-in-python

def pinger( job_q, results_q ):
    while True:
        ip = job_q.get()
        if ip is None:
            print(":(")
            break

        try:
            # raise Exception when ping raises error itself
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=subprocess.DEVNULL)
            results_q.put(ip)
            print("res", ip)
        except:
            pass

if __name__ == '__main__':
    print("run")
    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    for i in range(1,255):
        # TODO change to 169.254.x.y (169.254.0.0/16)
        # https://en.wikipedia.org/wiki/Reserved_IP_addresses
        jobs.put('192.168.178.{0}'.format(i))

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()
