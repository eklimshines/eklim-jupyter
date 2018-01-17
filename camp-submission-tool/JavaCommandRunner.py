import subprocess
from FileSystemNavigator import get_control_parameters, get_control_file_location

def get_java_tar_location():
    location_parameters = get_control_parameters('FileSystemInfo.json')
    java_tar_location = location_parameters['javaTarLocation']
    return java_tar_location

def run_java_command(message_type):
    java_tar_location = get_java_tar_location()
    control_file_location = get_control_file_location(message_type)
    java_command = "java -jar %s --messageType=%s --controlFile=%s" %(java_tar_location,message_type,
                                                                    control_file_location)
    print "Running %s" %(java_command)
    return subprocess.call(java_command)
