
from libdaq import *
from ctypes import *

def device_example(index):
    oldname = create_string_buffer(b'0', 100)
    errorcode = libdaq_device_get_name(0,byref(oldname),100)
    print("daq device name:",repr(oldname.value))
 
    libdaq_device_rename_byindex(index, b'DAQ_newname1')
    print("daq device rename by index to DAQ_newname1 success!")

    libdaq_device_rename_byname(b'DAQ_newname1',b'DAQ_newname2')
    print("daq device rename by index to DAQ_newname2 success!")

	#restore name
    libdaq_device_rename_byindex(index, oldname)
    print("daq device restore to old name: %s success!" % repr(oldname.value))

    #UID test
    print("setUID_byindex: blight at 1Hz")
    for i in range(0,2):
        libdaq_device_setUID_byindex(index,UID_state.ON)
        time.sleep(0.5)
        libdaq_device_setUID_byindex(index,UID_state.OFF)
        time.sleep(0.5)

    print("setUID_byName: blight at 1Hz")
    for i in range(0,2):
        libdaq_device_setUID_byname(oldname,UID_state.ON)
        time.sleep(0.5)
        libdaq_device_setUID_byname(oldname,UID_state.OFF)
        time.sleep(0.5)

    #get version
    print("libqab and device version:")
    version=libdaq_version() 
    libdaq_device_get_version(oldname,byref(version))
    print("library version:%d.%d.%d" % (version.libdaq_major,version.libdaq_minor,version.libdaq_micro))
    print("firmware version:%d.%d.%d" % (version.firmware_major,version.firmware_minor,version.firmware_micro))
    print("pcb version:%d" % version.pcb_ver)
    print("bom version:%d" % version.bom_ver)