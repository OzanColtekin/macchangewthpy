import subprocess as sb
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="-i  to use for interface")
    parse_object.add_option("-m","--mac",dest="mac_adress",help="-m to use for mac")
    return parse_object.parse_args()

def mac_changer(interface,mac_address):
    sb.call(["ifconfig", interface, "down"])
    sb.call(["ifconfig", interface, "hw", "ether", mac_address])
    sb.call(["ifconfig", interface, "up"])

def new_mac_control(interface):

    ifconfig = sb.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac Changer is started!")

(user_input,arguments) = get_user_input()
control_mac = new_mac_control(user_input.interface)
mac_changer(user_input.interface,user_input.mac_adress)

if user_input.interface == control_mac:
    print("Mac changed successfully!")
else:
    print("Mac changer cannot completed.")
