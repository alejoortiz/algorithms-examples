from netmiko import ConnectHandler
from threading import Thread
from queue import Queue

class SSH:

    def __init__(self,device_list):
        self.device_list = device_list

    def write_output(self,output,device):
        device_name = device.replace(".","_")
        file_name = f"{device_name}_output.txt"
        with open(file_name,'a') as file_output:
            file_output.write(output)

    def send_commands(self,q):
        device = q.get()
        device_parameters = {}
        device_parameters["device_type"] = "cisco_xr"
        device_parameters["ip"] = device
        device_parameters["username"] = "alejorti"
        device_parameters["password"] = "Jun2022al3j4ndr0*"
        with ConnectHandler(**device_parameters) as device_session:
            output = device_session.send_command("show clock")
            self.write_output(output, device)
        q.task_done()


    def create_workers(self,q):
        for device in range(len(self.device_list)):
            worker = Thread(target=self.send_commands, args=(q,))
            worker.start()
        q.join()

    def run(self):
        q = Queue(maxsize=0)
        for device in self.device_list:
            q.put(device)
        self.create_workers(q)

device_list = ["172.18.87.13","172.18.87.16"]
get_clock = SSH(device_list=device_list)
get_clock.run()