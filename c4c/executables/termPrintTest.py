import sys

print('Dive in')
test = 'qwerasdf'

def save_print_log(data):
    saveout = sys.stdout
    fsock = open('./saved_files/saved_post_metrics.log', 'a+')
    sys.stdout = fsock
    print(data)
    sys.stdout = saveout
    fsock.close()

save_print_log(test)

