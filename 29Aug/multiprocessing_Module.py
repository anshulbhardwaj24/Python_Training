import multiprocessing
import time

# print("Number of CPUs:", multiprocessing.cpu_count())

def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

# print("Number of CPUs:", multiprocessing.cpu_count())

tic = time.time()
if __name__ == "__main__":
    
    p1 =  multiprocessing.Process(target= sleepy_man)
    p2 =  multiprocessing.Process(target= sleepy_man)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    toc = time.time()


    print('Done in {:.4f} seconds'.format(toc-tic))





    # pool

# from multiprocessing import Pool

# import time

# work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


# def work_log(work_data):
#     print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
#     time.sleep(int(work_data[1]))
#     print(" Process %s Finished." % work_data[0])


# def pool_handler():
#     p = Pool(2)
#     p.map(work_log, work)


# if __name__ == '__main__':
#     pool_handler()