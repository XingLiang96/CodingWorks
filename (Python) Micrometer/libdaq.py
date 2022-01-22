#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 libdaq module

 For more information see *** or conact support@zishutech.com
 
 copyright@ZISHUTECH
'''
__author__ = 'ZhisuTech'

import ctypes
import platform
import os
# detect python version
architecture=platform.architecture()

#  load dll

dir=os.path.dirname(os.path.abspath(__file__))
if architecture[0] == '64bit':
    dll_path = os.path.join(dir,'./daqlib/MS64/daqlib.dll')
else:
    dll_path = os.path.join(dir,'./daqlib/MS32/daqlib.dll')

daqdll = ctypes.cdll.LoadLibrary(dll_path)


# API for devices
_libdaq_init = daqdll.libdaq_init
_libdaq_device_get_count = daqdll.libdaq_device_get_count
_libdaq_device_rename_byindex = daqdll.libdaq_device_rename_byindex
_libdaq_device_rename_byname = daqdll.libdaq_device_rename_byname
_libdaq_device_get_name = daqdll.libdaq_device_get_name
_libdaq_device_get_version=daqdll.libdaq_device_get_version
_libdaq_device_setUID_byindex=daqdll.libdaq_device_setUID_byindex
_libdaq_device_setUID_byname=daqdll.libdaq_device_setUID_byname

# API for GPIO
_libdaq_gpio_get_iocount=daqdll.libdaq_gpio_get_iocount
_libdaq_gpio_get_ioattrs=daqdll.libdaq_gpio_get_ioattrs
_libdaq_gpio_get_config=daqdll.libdaq_gpio_get_config
_libdaq_gpio_set_config=daqdll.libdaq_gpio_set_config
_libdaq_gpio_write_bit = daqdll.libdaq_gpio_write_bit
_libdaq_gpio_write_port = daqdll.libdaq_gpio_write_port
_libdaq_gpio_read_bit = daqdll.libdaq_gpio_read_bit
_libdaq_gpio_read_port = daqdll.libdaq_gpio_read_port

# API for DAC
_libdaq_dac_set_wavepara = daqdll.libdaq_dac_set_wavepara
_libdaq_dac_set_value=daqdll.libdaq_dac_set_value
_libdaq_dac_start = daqdll.libdaq_dac_start
_libdaq_dac_stop = daqdll.libdaq_dac_stop

# API for ADC
_libdaq_adc_config_channel=daqdll.libdaq_adc_config_channel
_libdaq_adc_config_channel_ex=daqdll.libdaq_adc_config_channel_ex
_libdaq_adc_singleSample=daqdll.libdaq_adc_singleSample
_libdaq_adc_set_sample_parameter    = daqdll.libdaq_adc_set_sample_parameter
_libdaq_adc_set_sample_parameter_ex = daqdll.libdaq_adc_set_sample_parameter_ex
_libdaq_adc_clear_buffer=daqdll.libdaq_adc_clear_buffer
_libdaq_adc_read_analog = daqdll.libdaq_adc_read_analog
_libdaq_adc_send_trigger=daqdll.libdaq_adc_send_trigger
_libdaq_adc_stop=daqdll.libdaq_adc_stop
_libdaq_adc_start_read=daqdll.libdaq_adc_start_read
_libdaq_adc_stop_read=daqdll.libdaq_adc_stop_read
_libdaq_adc_extractChannelData=daqdll.libdaq_adc_extractChannelData
_libdaq_adc_set_realtime=daqdll.libdaq_adc_set_realtime


# UID state value
UID_OFF = 0
UID_ON  = 1

# iomode 
IOMODE_IN=0        # input only
IOMODE_OUT=1       # output only
IOMODE_IN_OUT=2    # can be configured input or output
IOMODE_IN_AF=3     # can be configured input or Alternate function
IOMODE_OUT_AF=4    # can be configured output or Alternate function
IOMODE_IN_OUT_AF=5 # can be configured input, output or Alternate function

# ioconf
IOCONF_IN=0
IOCONF_OUT=1
IOCONF_AF=2

# channel range
CHANNEL_RANGE_0_P1V             =4  #range:0-1V
CHANNEL_RANGE_0_P2V             =8  #range:0-2V
CHANNEL_RANGE_0_P2V5            =12 #range:0-2.5V
CHANNEL_RANGE_0_P5V             =16 #range:0-5V
CHANNEL_RANGE_0_P10V            =20 #range:0-10V
CHANNEL_RANGE_N78mV125_P78mV125 =81 #range:+/-78.125mV
CHANNEL_RANGE_N156mV25_P156mV25 =82 #range:+/-156.25mV
CHANNEL_RANGE_N312mV5_P312mV5   =83 #range:+/-312.5mV
CHANNEL_RANGE_N0V256_P0V256     =22 #range:+/-0.256V
CHANNEL_RANGE_N0V512_P0V512     =23 #range:+/-0.512V
CHANNEL_RANGE_N0V625_P0V625     =84 #range:+/-0.625V
CHANNEL_RANGE_N1V_P1V           =24 #range:+/-1V
CHANNEL_RANGE_N1V024_P1V024     =25 #range:+/-1.024V
CHANNEL_RANGE_N1V25_P1V25   	=26 #range:+/-1.25V
CHANNEL_RANGE_N2V_P2V           =28 #range:+/-2V
CHANNEL_RANGE_N2V048_P2V048     =29 #range:+/-2.048V
CHANNEL_RANGE_N2V5_P2V5         =32 #range:+/-2.5V
CHANNEL_RANGE_N4V096_P4V096     =33 #range:+/-4.096V
CHANNEL_RANGE_N5V_P5V           =36 #range:+/-5V
CHANNEL_RANGE_N10V_P10V         =40 #range:+/-10V
CHANNEL_RANGE_0_P20mA           =64 #range:0-20mA
CHANNEL_RANGE_N20mA_P20mA       =65 #range:+/-20mA
CHANNEL_RANGE_0_P40mA           =66 #range:0-40mA
CHANNEL_RANGE_N40mA_P40mA       =67 #range:+/-40mA

# dac trigger mode
DAC_TRIGGER_MODE_AUTO=0x00  # auto start
DAC_TRIGGER_MODE_SOFT=0x01  # soft trigger
DAC_TRIGGER_MODE_HARD=0x02  # hard trigger,now is not supported

# adc sample mode
ADC_SAMPLE_MODE_SEQUENCE  = 0x00 #sequence mode
ADC_SAMPLE_MODE_GROUP     = 0x01 #group mode
ADC_SAMPLE_MODE_SYNC      = 0x02 #sync mode

# adc channel couple mode
ADC_CHANNEL_DC_COUPLE =0x00 #DC couple
ADC_CHANNEL_AC_COUPLE =0x01 #AC couple

ADC_CHANNEL_REFGND_RSE  =0x00 #referenced single ended
ADC_CHANNEL_REFGND_NRSE =0x01 #non referenced single ended
ADC_CHANNEL_REFGND_DIFF =0x02 #differencial

class libdaq_version(ctypes.Structure):
    _fields_ = [("libdaq_major",ctypes.c_uint8),   #Library major version
                ("libdaq_minor",ctypes.c_uint8),    #Library minor version 
                ("libdaq_micro",ctypes.c_uint8),   #Library micro version
                ("firmware_major",ctypes.c_uint8), #firmware major version
                ("firmware_minor", ctypes.c_uint8), #firmware minor version
                ("firmware_micro", ctypes.c_uint8), #firmware micro version
                ("pcb_ver", ctypes.c_uint8),           #PCB version
                ("bom_ver",ctypes.c_uint8)]            #BOM version

class ioattr(ctypes.Structure):
    _fields_ = [("iomode", ctypes.c_uint8)]

class dac_wavepara(ctypes.Structure):
    _fields_ = [("buf", ctypes.POINTER(ctypes.c_double)),
                ("buflen", ctypes.c_uint16),
                ("cycles", ctypes.c_uint32),
                ("frequency", ctypes.c_double),
                ("trigger_mode", ctypes.c_uint8)]

class adc_channelpara(ctypes.Structure):
    _fields_=[("channel",ctypes.c_uint8),
              ("range",ctypes.c_uint8),
              ("couplemode",ctypes.c_uint8),
              ("refground",ctypes.c_uint8) ]

class adc_samplepara(ctypes.Structure):
    _fields_=[("channel_list",ctypes.POINTER(ctypes.c_uint8)),
              ("channel_count",ctypes.c_uint8),
              ("sample_mode",ctypes.c_uint8), #sequence or group mode,sync mode
              ("frequency",ctypes.c_uint),  #sample rate (Hz)
              ("cycles",ctypes.c_uint),     #0:continues
              ("group_interval",ctypes.c_uint)] #only used in group mode(us)


# functions for device
def libdaq_init():
    """
	libdaq init function, must be call before call any API 
	Args: None
	Returns: errorcode
	Raises: None
	"""
    errorcode = _libdaq_init()
    return errorcode


def libdaq_device_get_count():
    """
	get DAQ device count in PC 
	Args: None
	Returns: daq device count
	"""
    return _libdaq_device_get_count()


def libdaq_device_rename_byindex(index, newname):
    """
	rename DAQ device by index
	Args: index
		  newname
	Returns: errorcode
	Raises: None
	"""
    errorcode = _libdaq_device_rename_byindex(index, newname)
    return errorcode

def libdaq_device_rename_byname(oldname, newname):
    """
	rename DAQ device by old name of DAQ decice
	Args: 	oldname
			newname
	Returns: errorcode
	Raises: None
	"""
    '''
        if not isinstance(oldname, (str, bytes)):
            raise TypeError("oldname type must be str or bytes")
        if not isinstance(newname, (str, bytes)):
            raise TypeError("newname type must be str or bytes")
    '''
    errorcode = _libdaq_device_rename_byname(oldname, newname)
    return errorcode


def libdaq_device_get_name(index,device_name,length):
    """
	get DAQ device name, 
	Args: 	index 
			device_name   
			length,buffer length
	Returns: errorcode
	Raises: None
	"""
    errorcode = _libdaq_device_get_name(index, device_name, length)
    return errorcode


def libdaq_device_get_version(device_name,version_p):
    """
	get DAQ decice version
	Args: 	device_name
			version
	Returns: errorcode
	Raises: None
	"""
    errorcode = _libdaq_device_get_version(device_name, version_p)
    return errorcode

def libdaq_device_setUID_byindex(index,state):
    """
	set UID LED state,when state=UID_ON,UID LED will turn on`
	Args: 	index
			state
	Returns: errorcode
	Raises: None
	"""
    if not isinstance(index, int):
        raise TypeError("index  type must be int")
    if not state in [UID_ON,UID_OFF]:
        raise TypeError("state  type must be value of UID_state")
    
    errorcode=_libdaq_device_setUID_byindex(index,ctypes.c_uint8(state))
    return errorcode
	

def libdaq_device_setUID_byname(device_name,state):
    """
	set UID LED state,when state=UID_ON,UID LED will turn on`
	Args: device_name
			state
	Returns: errorcode
	Raises: None
	"""
    if not state in [UID_ON,UID_OFF]:
        raise TypeError("state  type must be value of UID_state")		
    errorcode=_libdaq_device_setUID_byname(device_name,ctypes.c_uint8(state))
    return errorcode

def libdaq_adc_extractChannelData(all_data, ch_listlen,ch_index):
    all_datalen=len(all_data)
    ch_data=all_data[ch_index:all_datalen:ch_listlen]
    return ch_data



class libdaq_gpio(object):
    def __init__(self, device_name, module_name):
        self.__device_name = device_name
        self.__module_name = module_name
        (errorcode,self.__io_count)=self.get_iocount()

    def get_iocount(self):
        iocount=ctypes.c_uint8(0)
        errorcode=_libdaq_gpio_get_iocount(self.__device_name,self.__module_name,ctypes.byref(iocount))
        return errorcode,iocount.value

    def write_bit(self,ioIndex,BitVal):
        if not isinstance(ioIndex, int):
            raise TypeError("ioIndex  type must be int")

        if not isinstance(BitVal, int):
            raise TypeError("BitVal  type must be int")
        _BitVal=ctypes.c_uint8(BitVal)
        errorcode=_libdaq_gpio_write_bit(self.__device_name, self.__module_name, ioIndex, _BitVal)
        return errorcode

    def write_port(self,PortVal):
        if not isinstance(PortVal, list):
            raise TypeError("PortVal  type must be list")

        if len(PortVal) < self.__io_count:
            raise ValueError('input argurment PortVal size must same as iocount!')

        type_c_uint8_array_IO=ctypes.c_uint8*self.__io_count
        _PortVal=type_c_uint8_array_IO(*PortVal) # 操作符 * 展开参数 
        errorcode=_libdaq_gpio_write_port(self.__device_name,self.__module_name,ctypes.byref(_PortVal))
        return errorcode
        
    def read_bit(self,ioIndex):
        BitVal=ctypes.c_uint8(0)
        errorcode=_libdaq_gpio_read_bit(self.__device_name,self.__module_name,ioIndex,ctypes.byref(BitVal))
        return errorcode,BitVal.value
        
    def read_port(self):
        type_c_uint8_array_IO=ctypes.c_uint8*self.__io_count
        _PortVal=type_c_uint8_array_IO()
        errorcode=_libdaq_gpio_read_port(self.__device_name,self.__module_name,ctypes.byref(_PortVal))
        return errorcode , list(_PortVal)

class libdaq_dac(object):
    def __init__(self, device_name, module_name):
        self.__device_name = device_name
        self.__module_name = module_name

    def set_wavepara(self, wave_buf, cycles, frequency, trigger_mode):
        """
        libdaq dac config API
        Args:
            dac_wavepara,datalist,cycles,frequency,startmode
        Returns:
        Raises:
        """
        if not isinstance(wave_buf, list):
            raise TypeError("wave_buf  type must be list")

        dac_cfg=dac_wavepara()        
        type_double_arrary=ctypes.c_double*len(wave_buf) # double array
        
        buf=type_double_arrary(*wave_buf)
        buf_p=ctypes.POINTER(ctypes.c_double)()
        buf_p.contents=buf

        dac_cfg.buf=buf_p
        dac_cfg.buflen=len(wave_buf)
        dac_cfg.cycles=cycles #the data in buf output three times
        dac_cfg.frequency=frequency #10KHz
        dac_cfg.trigger_mode=trigger_mode # auto trigger mode

        errorcode = _libdaq_dac_set_wavepara(self.__device_name,self.__module_name,ctypes.byref(dac_cfg))
        return errorcode

    def set_value(self,value):
        _value = ctypes.c_double(value)
        errorcode =_libdaq_dac_set_value(self.__device_name,self.__module_name,_value)
        return errorcode

    def start(self):
        errorcode =_libdaq_dac_start(self.__device_name,self.__module_name)
        return errorcode

    def stop(self):
        errorcode =_libdaq_dac_stop(self.__device_name,self.__module_name)
        return errorcode


class libdaq_adc(object):
    def __init__(self, device_name, module_name):
        self.__device_name = device_name
        self.__module_name = module_name
    
    def config_channel_ex(self,channel,chrange,couplemode,refground):
        _channel = ctypes.c_ubyte(channel)
        _chrange = ctypes.c_ubyte(chrange)
        _couplemode = ctypes.c_ubyte(couplemode)
        _refground  = ctypes.c_ubyte(refground)
        errorcode=_libdaq_adc_config_channel_ex(self.__device_name,self.__module_name, _channel, _chrange, _couplemode, _refground)
        return errorcode

    def singleSample(self,channel_list):
        ch_len=len(channel_list)
        type_uint8_arrary=ctypes.c_uint8*ch_len # uint8 array,
        channel_list=type_uint8_arrary(*channel_list)
        channel_list_p=ctypes.POINTER(ctypes.c_uint8)()
        channel_list_p.contents=channel_list

        type_double_arrary=ctypes.c_double*ch_len # uint8 array,
        result_buf=type_double_arrary(0)
        result_buf_p=ctypes.POINTER(ctypes.c_double)()
        result_buf_p.contents=result_buf

        errorcode=_libdaq_adc_singleSample(self.__device_name,self.__module_name,channel_list_p, ch_len, result_buf_p)
        return errorcode,list(result_buf)

    def set_sample_parameter_ex(self,channel_list,sample_mode,frequency,cycles,group_interval):

        channel_count=len(channel_list)
        type_uint8_arrary=ctypes.c_uint8*channel_count # uint8 array,
        channel_list=type_uint8_arrary(*channel_list)
        channel_list_p=ctypes.POINTER(ctypes.c_uint8)()
        channel_list_p.contents=channel_list

        _channel_count=ctypes.c_uint(channel_count)
        _sample_mode=ctypes.c_uint(sample_mode)
        _frequency=ctypes.c_int(frequency)
        _cycles=ctypes.c_int(cycles)
        _group_interval=ctypes.c_int(group_interval)

        errorcode=_libdaq_adc_set_sample_parameter_ex(self.__device_name,self.__module_name,channel_list_p,_channel_count,_sample_mode,_frequency,_cycles,_group_interval)
        return errorcode

    def clear_buffer(self):
        errorcode=_libdaq_adc_clear_buffer(self.__device_name,self.__module_name)
        return errorcode

    def read_analog(self,datalen):
        actual_len=ctypes.c_uint(0)
        _datalen=ctypes.c_uint(datalen)

        type_double_arrary=ctypes.c_double*datalen # double array,
        data_buf=type_double_arrary(0)
        data_buf_p=ctypes.POINTER(ctypes.c_double)()
        data_buf_p.contents=data_buf

        errorcode=_libdaq_adc_read_analog(self.__device_name,self.__module_name, data_buf_p, _datalen, ctypes.byref(actual_len))
        return errorcode , list(data_buf[0:actual_len.value])

    def send_trigger(self):
        errorcode=_libdaq_adc_send_trigger(self.__device_name,self.__module_name)
        return errorcode   

    def stop(self):
        errorcode=_libdaq_adc_stop(self.__device_name,self.__module_name)
        return errorcode   
    
    def start_read(self):
        errorcode=_libdaq_adc_start_read(self.__device_name,self.__module_name)
        return errorcode

    def stop_read(self):
        errorcode=_libdaq_adc_stop_read(self.__device_name,self.__module_name)
        return errorcode

    def set_realtime(self,realtime_ms):
        _realtime_ms = ctypes.c_int(realtime_ms)
        errorcode=_libdaq_adc_set_realtime(self.__device_name,self.__module_name,_realtime_ms)
        return errorcode



class DAQUSB3212(object):
    def __init__(self, device_name):
        self.__device_name = device_name
        self.GPIOIN=libdaq_gpio(self.__device_name,b'GPIOIN')
        self.GPIOOUT=libdaq_gpio(self.__device_name,b'GPIOOUT')
        self.DAC1=libdaq_dac(self.__device_name,b'DAC1')
        self.DAC2=libdaq_dac(self.__device_name,b'DAC2')
        self.ADC1=libdaq_adc(self.__device_name,b'ADC1')
        pass

class DAQUSB3213(DAQUSB3212):
    pass

class DAQUSB3214(DAQUSB3212):
    pass

class DAQUSB1140(object):
    def __init__(self, device_name):
        self.__device_name = device_name
        self.GPIOIN=libdaq_gpio(self.__device_name,b'GPIOIN')
        self.GPIOOUT=libdaq_gpio(self.__device_name,b'GPIOOUT')
        self.DAC1=libdaq_dac(self.__device_name,b'DAC1')
        self.DAC2=libdaq_dac(self.__device_name,b'DAC2')
        self.ADC1=libdaq_adc(self.__device_name,b'ADC1')
        self.ADC2=libdaq_adc(self.__device_name,b'ADC2')
        pass

class DAQUSB1141(DAQUSB1140):
    pass