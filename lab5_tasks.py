"""Task 1 start"""

from math import sqrt
class point:

	def dist_between_points(self,a,b):
		dx=a
		dy=b
		print(a.x,b.x)
		dx=a.x-b.x
		dy=a.y-b.y
		print(dx,dy)
		dist=sqrt(dx**2+dy**2)
		print(dist)

p1=point()
p2=point()
p1.x=5
p2.x=4
p1.y=6
p2.y=4

p1.dist_between_points(p1,p2)

""" Task 1 end"""


""" Task 2 start"""

import copy

class point:
	"""this class represents point"""

class rectangle:
	"""this class represents a rectangle"""

	def find_center(self,rect):
	        p = point()
       		p.x = rect.corner.x + rect.width/2
        	p.y = rect.corner.y + rect.height/2
        	return p

	def print_point(self,p):
	        print('(%g,%g)'%(p.x,p.y))

	def move_rectangle(self,rect,dx,dy):
		rect.width += dx
		rect.height += dy

box=rectangle()
box.width=100.0
box.height=200.0
box.corner=point()
box.corner.x=0.0
box.corner.y=0.0
box2=copy.deepcopy(box)

center=box.find_center(box)
box.print_point(center)
box.move_rectangle(box,70,120)
print(box.width,box.height)
box2.move_rectangle(box2,90,140)
print(box2.width,box2.height)

""" Task 2 end """


""" Task 3 start """

class Time:
	"""this class represents time"""

	"""def print_time(self,t):
		print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))"""

time=Time()
time.hour=9
time.minute=35
time.second=25
def print_time(t):
	print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))

print_time(time)

""" Task 3 end """

""" Task 4 start """

class Time:
	"""this class represents time"""

t1=Time()
t2=Time()

t1.hour=10
t1.minute=55
t1.second=25

t2.hour=10
t2.minute=45
t2.second=30

def print_time(t):
	print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))
 
def is_after(t1, t2):
    t1_total_seconds = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_total_seconds = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_total_seconds > t2_total_seconds
     
print_time(t1)
print_time(t2)

print(is_after(t1,t2))

""" Task 4 end """

""" Task 5 start """

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("x =", self.x)
        print("y =", self.y)

point = Point()
point.print_point()

point = Point(10)
point.print_point()

point = Point(20, 30)
point.print_point()

#String method
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

point = Point()
print(point)

point = Point(10)
print(point)

point = Point(10, 15)
print(point)

#third part
class Point(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
         
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
         
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point
         
point1 = Point(1, 3)
point2 = Point(4, 5)
 
print(point1 + point2)

""" Task 5 end """

""" Task 6 start """

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0]
            point_.y += self.y + other[1]
        return point_

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

point1 = Point(1, 6)
point2 = (5, 2)
point3 = point1 + point2
point4 = point2 + point1
print(point3,point4)
print(point3+point4)

""" Task 6 end """


""" Task 7 start """

class Kangaroo:
    """A Kangaroo is a marsupial."""
    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents or []

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch('function call')
roo.put_in_pouch('new wallet')
roo.put_in_pouch('new car keys')
roo.put_in_pouch('new function call')

print(kanga)
print(roo)

""" Task 7 end """


""" Task 8 start """

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0]
            point_.y += self.y + other[1]
        return point_

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

point1 = Point(1, 6)
point2 = (7, 5)
point3 = point1 + point2
point4 = point2 + point1
print(point3,point4)
print(point3+point4)

""" Task 8 end """

""" Task 11 start """

class IPv4address():
        def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
                self.ip=ip
                self.nm=nm
        def __str__(self):
                ipformat=""
                for ips in self.ip:
                        ipformat=ipformat+str(ips)+"."
                return('the address is:'+ ipformat)  
        def getNetwork(self,nadd=[0,0,0,0]):
                self.nadd=nadd[0:3]
                return self.nadd
        def getMask(self,mask=[0,0,0,0]):
                self.mask=self.nm
                return self.mask
        def getAddress(self,ipadd=[0,0,0,0]):
                self.ipadd=self.ip
                return self.ipadd

myip=IPv4address([192,168,1,1],[255,255,255,255])
mynw=myip.getNetwork([192,168,10,5])
mymask=myip.getMask()
myipad=myip.getAddress()
print(myip)
print(mynw)
print(mymask)
print(myipad)

""" Task 11 end """


""" Task 12 start """
"""
import random
import sys

def subnet_calc():
    try:
        print("\n")

        #Checking IP address validity
        while True:
            ip_address = input("Enter an IP address: ")

            #Checking octets            
            a = ip_address.split('.')

            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        #Checking Subnet Mask validity
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            #Checking octets            
            b = subnet_mask.split('.')

            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break

            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue

	############# Application #1 - Part #2 #############

        #Algorithm for subnet identification, based on IP and Subnet Mask

        #Convert mask to binary string
        mask_octets_padded = []
        mask_octets_decimal = subnet_mask.split(".")
        #print mask_octets_decimal

        for octet_index in range(0, len(mask_octets_decimal)):

            #print bin(int(mask_octets_decimal[octet_index]))

            binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]
            #print binary_octet

            if len(binary_octet) == 8:
                mask_octets_padded.append(binary_octet)

            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octets_padded.append(binary_octet_padded)

        #print mask_octets_padded

        decimal_mask = "".join(mask_octets_padded)
        #print decimal_mask   #Example: for 255.255.255.0 => 11111111111111111111111100000000

        #Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = decimal_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return positive value for mask /32

        #print no_of_zeros
        #print no_of_ones
        #print no_of_hosts

        #Obtaining wildcard mask
        wildcard_octets = []
        for w_octet in mask_octets_decimal:
            wild_octet = 255 - int(w_octet)
            wildcard_octets.append(str(wild_octet))

        #print wildcard_octets

        wildcard_mask = ".".join(wildcard_octets)
        #print wildcard_mask

        ############# Application #1 - Part #3 #############

        #Convert IP to binary string
        ip_octets_padded = []
        ip_octets_decimal = ip_address.split(".")

        for octet_index in range(0, len(ip_octets_decimal)):

            binary_octet = bin(int(ip_octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                ip_octets_padded.append(binary_octet_padded)

            else:
                ip_octets_padded.append(binary_octet)

        #print ip_octets_padded

        binary_ip = "".join(ip_octets_padded)

        #print binary_ip   #Example: for 192.168.2.100 => 11000000101010000000001001100100

        #Obtain the network address and broadcast address from the binary strings obtained above

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        #print network_address_binary

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        #print broadcast_address_binary

        net_ip_octets = []
        for octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[octet:octet+8]
            net_ip_octets.append(net_ip_octet)

        #print net_ip_octets

        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        #print net_ip_address

        network_address = ".".join(net_ip_address)
        #print network_address

        bst_ip_octets = []
        for octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[octet:octet+8]
            bst_ip_octets.append(bst_ip_octet)

        #print bst_ip_octets

        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        #print bst_ip_address

        broadcast_address = ".".join(bst_ip_address)
        #print broadcast_address

        #Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

        ############# Application #1 - Part #4 #############

        #Generation of random IP in subnet
        while True:
            generate = input("Generate random ip address from subnet? (y/n)")

            if generate == "y":
                generated_ip = []

                #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(bst_ip_address):
                    #print indexb, oct_bst
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print indexn, oct_net
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                #Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                #IP address generated from the subnet pool
                #print generated_ip
                y_iaddr = ".".join(generated_ip)
                #print(y_iaddr)

                print("Random IP address is: %s" % y_iaddr)
                print("\n")
                continue

            else:
                print("Exiting !\n")
                break

    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

subnet_calc()
"""

""" Task 12 end """
