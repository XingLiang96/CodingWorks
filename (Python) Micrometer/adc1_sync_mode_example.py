def adc1_sync_mode_example(device):
    channellist=[0,2]

    sample_mode=libdaq.ADC_SAMPLE_MODE_SYNC
    frequency=10000 #1kHz
    cycles=10

    group_interval=0

    device.ADC1.set_sample_parameter_ex(channellist,sample_mode,frequency,cycles,group_interval)
    device.ADC1.clear_buffer()
    device.ADC1.send_trigger()
    time.sleep(2)
    data_len=cycles*len(channellist)
    (errorcode,result)=device.ADC1.read_analog(data_len)

    #print("磨耗尺的压缩量为（单位：mm）:")
    for ch_index in range(0,len(channellist)):
        ch_data=libdaq.libdaq_adc_extractChannelData(result,len(channellist),ch_index)
        a=0
        for data in ch_data :
            #bb=sys.stdout.write("%2.4f " % (-3.82725*(data)+18.978))
            b=data
            a=a+b
        aver=a/cycles
        gg="%2.4f " %(-3.82725*(aver)+18.978)
        print(gg)