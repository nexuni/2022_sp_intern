"""
Abstract Data Types
Learning Materials: 
	* http://web.mit.edu/6.031/www/sp22/classes/10-abstract-data-types/
	* http://web.mit.edu/6.031/www/sp22/classes/11-abstraction-functions-rep-invariants/

Brief Introduction on Nexuni Ecosystem
---------------------------------------
+ 	NexDevice: Every single embedded device
+       |
+    NexSite : Every Nexuni site
+		|
+	NexDomain: Every LAN domain or Industry type
+		|
+	  Nexuni : Nexuni Universe
---------------------------------------

The hierarchy shows the relationship
between Nexuni devices, sites, and domains. 
It is used to keep track of all device information, 
states, and teleoperations
"""
class NexDevice(object):
	"""
	Represents an embedded device with active OS running. 

	Abstraction Function:
		AF(ip_address, os, arch, **deviceinfo) = a nexuni device 
			running at `ip_address` on operating system - `os` 
			and `arch` cpu architecture. Characterized by
			deviceinfo
	
	Rep: 
		ip_address: string
		os: string
		arch: string
		deviceinfo: dict, or expand to self attributes

	Functions
	------------------------------------------------
	Creators:
		@classmethod
		create_nexdevice_from_dump(dump_string) -> Nexdevice

	Observers:
		get_battery_percentage() -> double
	    get_docker_version() -> string
	    get_service_status(srv_name) -> bool
	
	Producers:
		get_ip_search_range(subnet) -> string

	Mutators:
		start_service(srv)
		stop_service(srv)
	"""
	def __init__(self):
		# Constructor dummy initialization
		pass

	@classmethod
	def create_nexdevice_from_dump(dump_string):
		"""
		Create a NexDevice object based on deviceinfo
		encoded in dump_string.
		Input:
			dump_string: string in json format that encodes
				all the device info. 
		Output:
			valid NexDevice object
		"""
		pass

	def get_battery_percentage():
		"""
		Return battery voltage. 
		Output:
			battery voltage (double)
		"""
		pass

	def get_docker_version():
		"""
		Return docker version string. 
		Output:
			a docker version string with the following 
			format: '-{OS}-{ARCH}'
		"""
		pass

	def get_ip_search_range(subnet):
		"""
		Given ipv4 subnet, return a tuple
		of start search ip and end search ip

		https://www.calculator.net/ip-subnet-calculator.html
		Input:
			subnet: ex. 255.255.255.0
		Output:
			Usable Host IP Range: ("192.168.2.1", "192.168.2.254")
		"""
		pass

	def get_service_status(srv):
		"""
		Get the status of service `srv`
		Input:
			srv: service name
		Output:
			current service status (Bool)
		"""
		pass

	def start_service(srv):
		"""
		Go through the services on this device
		and start the service `srv`
		Input:
			srv: service name
		"""
		pass

	def stop_service(srv):
		"""
		Go through the services on this device
		and stop the service `srv`
		Input:
			srv: service name
		"""
		pass

import json

nd_dump = json.dumps({"ip_address": "192.168.2.10", 
	"os": "ubuntu.18.04", 
	"arch": "aarch-64",
	"battery": 76.3, "services": [{"cloud_sync_service": {"status": True, "start_time": 167462514, 
		"log_path": "/log/cloud_1"}}, {"watchdog_service": {"status": False, "start_time": 167461514, 
		"log_path": "/log/watchdog_1"}}, {"memory_management_service": {"status": True, "start_time": 151662514, 
		"log_path": "/log/mem_1"}}]
	})

nd = NexDevice.create_nexdevice_from_dump(nd_dump)
assert nd.get_docker_version() == "-ubuntu.18.04-aarch-64"
assert nd.get_battery_percentage() == 76.3
assert nd.get_ip_search_range("255.255.254.0") == ("192.168.2.1", "192.168.3.254")

nd.start_service("watchdog_service")
assert nd.get_service_status("watchdog_service") == True

nd.stop_service("memory_management_service")
assert nd.get_service_status("memory_management_service") == False

print("Success")
