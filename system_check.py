from datetime import datetime # For working with dates and times.
from getpass import getuser # For determining logged in user.
import platform # For accessing underlying platform information.
import psutil # For obtaining information on system utilization (e.g. disk, CPU, memory and network).

class SystemCheck:
	'''
	Class containing functionality for checking system information, disk usage,
	CPU usage, memory usage and network usage.
	'''
	def __init__(self):
		'''Initializes the object with important attributes.'''
		self.os = platform.platform() # Gets detailed name of operating system.

	def check_system_info(self):
		'''
		Displays some information about the system such as the operating system,
		machine name, user logged in and the boot time.
		''' 
		machine_name = platform.uname().node # Gets name of machine.
		username = getuser() # Gets the user that is currently logged in.
		boot_time_timestamp = psutil.boot_time() # Gets a timestamp of the boot time.
		boot_time = datetime.fromtimestamp(boot_time_timestamp) # Converts the timestamp into a datetime object.
		
		# Prints system information.
		print('------SYSTEM INFORMATION------')
		print(f'OS: {self.os}') 
		print(f'Machine Name: {machine_name}')
		print(f'Logged in User: {username}') 

		# Prints the boot time in the format dd/mm/yyyy hh:mm:ss
		print(f'Boot Time: {boot_time.day}/{boot_time.month}/{boot_time.year} {boot_time.hour}:{boot_time.minute}:{boot_time.second}\n')
		
	def check_disk_usage(self):
		'''
		Displays disk usage information for the root directory ('C:' for Windows
		and '/' for Linux/macOS), and displays a warning if the disk is over 80% full.
		'''
		# Checks the OS assigns the respective root directory.
		if self.os.startswith('Windows'):
			disk = 'C:'
		else:
			disk = '/'

		try:
			disk_usage = psutil.disk_usage(disk) # Obtains disk usage information.
			total = disk_usage.total / (1024 ** 3) # Calculates the total disk size in GB.
			used = disk_usage.used / (1024 ** 3) # Calculates the used space in GB.
			free = total - used # Calculates the free disk space in GB.
			percentage_used = (used / total) * 100 # Calculates percentage disk spaced used.

			# Prints information about the disk.
			print('----------DISK USAGE----------')
			print(f'Disk: {disk[0]}')
			print(f'Total: {total:,.2f}GB')
			print(f'Used : {used:,.2f}GB')
			print(f'Free: {free:,.2f}GB')
			print(f'% Disk used: {percentage_used:.2f}%')

			# Prints a warning message if the disk space is less than 20%.
			if percentage_used > 80:
				print(f'Warning: Available disk space is less than 20%.')
			print()
		except OSError: 
			# Prints an error message if the drive does not exist.
			print(f'{disk} does not exist.') 

	def check_cpu_usage(self):
		'''
		Displays CPU frequency, number of physical cores and CPU Usage, and 
		displays a warning if the CPU Usage exceeds 80%. 
		'''
		cpu_frequency = psutil.cpu_freq().current # Obtains CPU Frequency
		cpu_usage = psutil.cpu_percent(1) # Determines CPU usage (%) in 1 second.
		cpu_cores = psutil.cpu_count(logical=False) # Determines number of physical CPU cores.

		# Prints information about the CPU.
		print('-----------CPU USAGE-----------')
		print(f'CPU Frequency: {cpu_frequency}')
		print(f'Physical Cores: {cpu_cores}')
		print(f'CPU Usage: {cpu_usage}%')

		# Prints a warning message if the CPU Usage is more than 80%.
		if cpu_usage > 80:
			print('Warning: CPU Usage exceeds 80%')
		print()

	def check_memory_usage(self):
		'''
		Displays memory (RAM) usage information and displays a warning if the available
		memory is less than 500MB.
		'''
		total = psutil.virtual_memory().total / (1024 ** 2) # Calculates total memory in MB.
		used = psutil.virtual_memory().used / (1024 ** 2) # Calculates used memory in MB.
		free = total - used # Calculates free memory in MB.
		percentage_used = (used / total) * 100 # Calculates percentage of memory used.
		
		# Prints memory information.
		print('---------MEMORY USAGE---------')
		print(f'Total: {total:,.2f}MB')
		print(f'Used: {used:,.2f}MB')
		print(f'Free: {free:,.2f}MB')
		print(f'% Memory used: {percentage_used:.2f}%')

		# Prints a warning message if the available memory is less than 500MB. 
		if free < 500:
			print('Warning: Available memory is less than 500MB')
		print()

	def check_network_usage(self):
		'''Displays network usage information since connected to the network.'''
		network_usage = psutil.net_io_counters() # Obtains network usage information.
		mb_sent = network_usage.bytes_sent / (1024 ** 2) # Calculates MB of data sent.
		mb_received = network_usage.bytes_recv / (1024 ** 2) # Calculates MB of data received .
		packets_sent = network_usage.packets_sent # Obtains number of data packets sent.
		packets_received = network_usage.packets_recv # Obtains number of data packets received.

		# Prints network usage information.
		print('---------NETWORK USAGE---------')
		print(f'MB sent: {mb_sent:,.2f}')
		print(f'MB received: {mb_received:,.2f}\n')
		print(f'Packets sent: {packets_sent:,d}')
		print(f'Packets received: {packets_received:,d}\n')


if __name__ == '__main__':
	# Creates a SystemCheck object and call each of its methods.
	system_check = SystemCheck()
	system_check.check_system_info() 
	system_check.check_disk_usage() 
	system_check.check_cpu_usage() 
	system_check.check_memory_usage()
	system_check.check_network_usage()