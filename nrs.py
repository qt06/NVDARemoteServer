import time
import threading
import server


def start_server(port, password):
	ns = server.Server(port, password)
	server_thread = threading.Thread(target=ns.run)
	server_thread.daemon = True
	server_thread.start()
	print 'server has started'
	while True:
		time.sleep(1)


start_server(6837, '6768')