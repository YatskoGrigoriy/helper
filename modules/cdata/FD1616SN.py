#! /usr/bin/python3
import os



class C_DATA_Base_FD1616SN:


    def base_info(self, ip, community):
        # Uptime
        r_uptime = ''
        uptime = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.1.2.1.1.5')
        for u in uptime:
            t = u.split('=')[1].split(' ')
            r_uptime = t[-3] + ' ' + t[-2] + ' ' + t[-1]
        cpu = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.34592.1.3.100.1.8.1.0')
        for r_cpu in cpu:
            r_cpu
        c = r_cpu.split('=')[1].split(':')[-1].strip()    

        temp = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.34592.1.3.100.1.8.6')
        for r_temp in temp:
            r_temp    
        tmp = str(int(r_temp.split('=')[1].split(':')[-1].strip()) /10 )
       
        
        total_memory = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.34592.1.3.100.1.8.2.0')
        for r_mem in total_memory:
            r_mem   
        total_mem = str(int(r_mem.split('=')[1].split(':')[-1].strip()))

        free_memory = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.34592.1.3.100.1.8.3.0')
        for r_fmem in free_memory:
            r_fmem   
        free_mem = str(int(r_fmem.split('=')[1].split(':')[-1].strip()))
        
       
        
        return {'r_uptime': r_uptime, 'r_cpu': c , 'r_temp': tmp , 'total_mem': total_mem, 'free_mem': free_mem}

    def port_onu_active(self, ip, community):
        
        r_all_onu_active = []
        r_port_tx_power = []
        r_port_volt = []
        r_port_holding = []
        r_port_name = []
        r_port_status = []
        r_port_oper_status = []
        
        all_onu_active = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.8')
        for ana in all_onu_active:
            r_all_onu_active.append({'port_id': ana.split('=')[0].split('.')[-1].strip(),
                                     'onu_count': ana.split('=')[1].split(':')[-1].strip(), 
                                     'port_holding': '', 'pon_status' : '', 
                                     'pon_oper_status': '',
                                     'port_tx_power': '', 'port_volt': ''})

        port_tx_power = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.5.1.6')
        for tx in port_tx_power:
            r_port_tx_power.append({'port_id': tx.split('=')[0].split('.')[-1].strip(),
                                    'port_tx_power': str(int(tx.split('=')[1].split(':')[-1].strip()) / 100)}) 

        port_volt = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.5.1.4')
        for volt in port_volt:
            r_port_volt.append({'port_id': volt.split('=')[0].split('.')[-1].strip(),
                                'port_volt': str(int(volt.split('=')[1].split(':')[-1].strip()) / 100000)})                                                       

        port_holding = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.7')
        for ph in port_holding:
            r_port_holding.append({'port_id': ph.split('=')[0].split('.')[-1].strip(),
                                   'port_holding': ph.split('=')[1].split(':')[-1].strip()})

        port_name = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.21')
        for pn in port_name:
            r_port_name.append({'port_id': pn.split('=')[0].split('.')[-1].strip(),
            'port_name': pn.split('=')[1].split(':')[-1].strip().strip('"')}) 

        port_status = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.5')
        for st in port_status:
            r_port_status.append({'port_id' : st.split('=')[0].split('.')[-1].strip(),
            'pon_status' : st.split('=')[1].split(':')[-1].strip()})
            port_oper_status = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.2.1.2.2.1.5.' + 
            str(st.split('=')[0].split('.')[-1].strip()))
            for pon_oper in port_oper_status:
                r_port_oper_status.append({'port_id': st.split('=')[0].split('.')[-1].strip(),  
                'pon_oper_status':pon_oper.split(':')[-1].strip()})
                
            
                             

        for item in r_all_onu_active:

            try:
                for item0 in r_port_volt:
                    if item['port_id'] == item0['port_id']:
                        item['port_volt'] = item0['port_volt']
            except:
                pass
            
            try:
                for item1 in r_port_tx_power:
                    if item['port_id'] == item1['port_id']:
                        item['port_tx_power'] = item1['port_tx_power']
            except:
                pass

            try:
                for item2 in r_port_holding:
                    if item['port_id'] == item2['port_id']:
                        item['port_holding'] = item2['port_holding']
            except:
                pass

            try:
                for item3 in r_port_status:
                    if str(item['port_id']) == item3['port_id']:
                        item['pon_status'] = item3['pon_status']   
            except:
                pass 
            try:
                for item5 in  r_port_oper_status:
                    if str(item['port_id']) == item5['port_id']:
                        item['pon_oper_status'] = item5['pon_oper_status']   
            except:
                pass     

            try:
                for item4 in r_port_name:
                    if str(item['port_id']) == item4['port_id']:
                        item['port_id'] = item4['port_name']   
            except:
                pass 
            
        return r_all_onu_active       

    def eth_status(self, ip, community):

        r_all_ethernet_name = []
        r_all_ethernet_status = []
        r_all_oper_status = []

        ethernet_name = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.2.1.1.4')
        for eth_name in ethernet_name:
            r_all_ethernet_name.append({'eth_id': eth_name.split('=')[0].split('.')[-1].strip(),
            'eth_name': eth_name.split('=')[1].split(':')[-1].strip(), 'eth_status' : '', 'eth_oper_status': ''})
                


        ethernet_status = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.2.1.1.6')
        for eth in ethernet_status:
            r_all_ethernet_status.append({'eth_id': eth.split('=')[0].split('.')[-1].strip(),
            'eth_status': eth.split('=')[1].split(':')[-1].strip()})
            oper_status = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.2.1.2.2.1.5.' + 
            str(eth.split('=')[0].split('.')[-1].strip()))
            for eth_oper in oper_status:
                r_all_oper_status.append({'eth_id': eth.split('=')[0].split('.')[-1].strip(),  
                'eth_oper_status':eth_oper.split(':')[-1].strip()})        

          


        for item in r_all_ethernet_name:
            try:
                for item2 in r_all_ethernet_status:
                    if item['eth_id'] == item2['eth_id']:
                        item['eth_status'] = item2['eth_status']
            except:
                pass 
            try:
                for item3 in r_all_oper_status:
                    if item['eth_id'] == item3['eth_id']:
                        item['eth_oper_status'] = item3['eth_oper_status']
            except:
                pass  
              
        return r_all_ethernet_name


    def port_onu_count(self, ip, community):

        def onu_port_id(ID):
    
            r = hex(int(ID))
            port_id = (int(r[-4]+r[-3], 16))
            onu_id = (int(r[-2]+r[-1], 16))

            return({'port_id': port_id,'onu_id' : onu_id})

        r_all_port_name = []
        r_all_onu_desc = []
        r_all_onu_oper_status = []
        r_all_onu_user_mac = []
        r_all_onu_serial_num = []
        r_all_onu_signal = []
        r_all_onu_distance = []
        
        # ALL_PORT NAME
        port_name = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.21')
        for pn in port_name:
            r_all_port_name.append({
            'id': pn.split('=')[0].split('.')[-1].strip(),
            'port_name': pn.split('=')[1].split(':')[-1].strip().strip('"')
            })
        # ALL_ONU_DESC
        all_onu_desc = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.1.1.2')
        for desc in all_onu_desc:
            r_all_onu_desc.append({
            'id': desc.split('=')[0].split('.')[-1].strip(),
            'port_id' : '',
            'onu_id'  : '',
            'onu_desc': desc.split('=')[1].split(':')[-1].strip(),
            'port' : '',
            'onu_status' : '',
            'onu_mac_serial' : '',
            'user_mac': [],
            'onu_signal' : '',
            'onu_lenght' : '',
            
             })
        # ALL_ONU_STATUS
        all_onu_oper_status = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.8.4.1.1.7')
        for status in all_onu_oper_status:
            r_all_onu_oper_status.append({
                'id' : status.split('=')[0].split('.')[-1].strip(),
                'onu_status' : status.split('=')[1].split(':')[-1].strip()
            })
        # ALL_ONU_USER_MAC_ADDRESS
        all_onu_user_mac = os.popen('snmpwalk -v2c -c ' + community + ' -t 2 ' + ip + ' iso.3.6.1.4.1.34592.1.5.1.1.2.19.3.1.2.1')
        for umac in all_onu_user_mac:
            r_all_onu_user_mac.append({
                'onu_id' : umac.split('=')[0].split('.')[-3].strip(),
                'port_id' : umac.split('=')[0].split('.')[-4].strip(),
                'user_mac' : umac.split('=')[1].split(':')[-1].strip().replace(' ', ':')
            })
        # ALL_ONU_SIGNAL
        all_onu_signal = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.4.1.4')
        for aos in all_onu_signal:
            r_all_onu_signal.append({'id': aos.split('=')[0].split('.')[-3].strip(),
                                     'onu_signal': str(int(aos.split('=')[1].split(':')[-1].strip()) / 10)})
        # ALL_ONU_DISTANCE
        all_onu_distance = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.1.1.9')
        for distance in all_onu_distance:
            r_all_onu_distance.append({'id': distance.split('=')[0].split('.')[-1].strip(),
                                     'onu_lenght': distance.split('=')[1].split(':')[-1].strip()})
        # ALL_ONU_SERIAL_NUM
        all_onu_serial_num = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.8.4.1.1.3')
        for serial in all_onu_serial_num:
            r_all_onu_serial_num.append({
                'id' : serial.split('=')[0].split('.')[-1].strip(),
                'onu_mac_serial' : serial.split('=')[1].split(':')[-1].strip().replace(' ', '')

            })




        
        for item in r_all_onu_desc:
            try:
                for item1 in r_all_onu_oper_status:
                    if item['id'] == item1['id']:
                        item['onu_status'] = item1['onu_status']
            except:
                pass            
            try:
                for item2 in r_all_port_name:
                    rs = onu_port_id(item['id'])
                    if str(rs['port_id']) == item2['id']:
                        item['port'] = str(item2['port_name']) + ':' + str(rs['onu_id'])
                        item['port_id'] = str(rs['port_id'])
                        item['onu_id'] = str(rs['onu_id'])
            except:
               pass

            try:
                for item3 in r_all_onu_user_mac:
                    if item['port_id'] == str(item3['port_id']) and item['onu_id'] == item3['onu_id']:
                        item['user_mac'].append(item3['user_mac'])
            except:
                pass 

            try:
                for item4 in r_all_onu_signal:
                    if  item['id'] == item4['id']:
                        item['onu_signal'] = item4['onu_signal']
            except:
                pass 

            try:
                for item5 in r_all_onu_distance:
                    if item['id'] == item5['id']:
                        item['onu_lenght']  = item5['onu_lenght'] 
            except:
                pass 
            try:
                for item6 in r_all_onu_serial_num:
                    if item['id'] == item6['id']:
                        item['onu_mac_serial'] = item6['onu_mac_serial']
            except:
                pass                          
        # print(r_all_onu_desc)         
        return r_all_onu_desc        

    def onu_info(self, ip, community, OnuId):
        all = []
        #Port_N
        def port_n(OnuId):
            p_name = 'undefined'
            r = hex(int(OnuId))
            port_id = int(r[-4] + r[-3], 16)
            onu_id = int(r[-2] + r[-1], 16)

            port_name = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.3.1.1.21')
            for pn in port_name:
            
                if int(pn.split('=')[0].split('.')[-1]) == port_id:
                    p_name = pn.split('=')[1].split(':')[-1].strip().strip('"')
                
                    
            return p_name + ':' + str(onu_id)

        def onu_port_id(ID):
    
            r = hex(int(ID))
            port_id = (int(r[-4]+r[-3], 16))
            onu_id = (int(r[-2]+r[-1], 16))

            return({'port_id': port_id,'onu_id' : onu_id})    

        #Status_Wan
        status_wan = []
        onuStatusWan = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + '  .1.3.6.1.4.1.17409.2.8.5.1.1.5.' + OnuId)
        for sts in onuStatusWan:
            status_wan.append(sts.split('=')[1].split(':')[-1].strip('"').strip())

        #User_Mac
        onu_user_mac = []
        onuUserMac = os.popen('snmpwalk -v2c -c ' + community + ' -t 2 ' + ip + ' iso.3.6.1.4.1.34592.1.5.1.1.2.19.3.1.2.1.0.' + 
        str(onu_port_id(OnuId)['port_id']) + '.' + str(onu_port_id(OnuId)['onu_id']))
        for um in onuUserMac:
             onu_user_mac.append({'user_port': um.split('=')[0].split('.')[-2].strip(),
                                  'user_mac': um.split('=')[1].split(':')[-1].strip().replace(' ', ':')})

         #User_Vlan
        onu_user_vlan = []
        onuUserVlan = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.3.7.3.1.1.7.' + OnuId)
        for uvl in onuUserVlan:
            onu_user_vlan.append({'port_vlan' : uvl.split('=')[0].split('.')[-1].strip(),
            'user_vlan' : uvl.split('=')[1].split(':')[-1].strip()})
           

        # Onu_SignalRx
        onuSignalRx = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.4.1.4.' + OnuId)
        for srx in onuSignalRx:
            onu_signal_rx = int(srx.split('=')[1].split(':')[-1].strip('"').strip()) / 10

        # Onu_SignalTx
        onuSignalTx = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.4.1.5.' + OnuId)
        for stx in onuSignalTx:
            onu_signal_tx = int(stx.split('=')[1].split(':')[-1].strip('"').strip()) / 100
        #Onu_distance
        onuDistance = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.1.1.9.' + OnuId)
        for d in onuDistance:
            onu_distance = d.split('=')[1].split(':')[-1].strip('"').strip()

        # Onu_Vendor
        onuVendor = os.popen(
            'snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.1.1.5.' + OnuId)
        for v in onuVendor:
            onu_vendor = v.split('=')[1].split(':')[-1].strip('"').strip()

        # Onu_Model
        onuModel = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' 1.3.6.1.4.1.17409.2.8.4.1.1.6.' + OnuId)
        for m in onuModel:
            onu_model = m.split('=')[1].split(':')[-1].strip('"').strip()

        # Onu_Hard
        onuVerHard = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.1.1.14.' + OnuId)
        for vh in onuVerHard:
            onu_ver_hard = vh.split('=')[1].split(':')[-1].strip('"').strip()
        # Onu_Soft
        onuVerSoft = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.17409.2.8.4.2.1.6.' + OnuId)
        for vs in onuVerSoft:
            onu_ver_soft = vs.split('=')[1].split(':')[-1].strip('"').strip()

        #OnuLog
        OnuLog = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.1.1.103.' + OnuId)
        for l in OnuLog:
            onu_log = l.split('=')[1].split(':')[-1].strip('"').strip()

        # OnuDesc
        OnuDesc = os.popen(
        'snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.1.1.2.' + OnuId)
        for ds in OnuDesc:
            onu_desc = ds.split('=')[1].split(':')[-1].strip('"').strip()



         # OnuVolt
        OnuVolt = os.popen(
        'snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.4.1.7.' + OnuId)
        for volt in OnuVolt:
            onu_volt = int(volt.split('=')[1].split(':')[-1].strip('"').strip()) / 100000

         # OnuTemp
        OnuTemp = os.popen(
        'snmpwalk -v2c -c ' + community + ' ' + ip + ' .1.3.6.1.4.1.17409.2.8.4.4.1.8.' + OnuId)
        for temp in OnuTemp:
            onu_temp = int(temp.split('=')[1].split(':')[-1].strip('"').strip()) / 100


        all.append({'port': port_n(OnuId), 'status_wan': status_wan, 'signal_rx': str(onu_signal_rx), 'signal_tx': onu_signal_tx,
                 'distance': onu_distance,'mac_ip': [], 'log': onu_log, 'vendor': onu_vendor,
                 'model': onu_model,'ver_hard': onu_ver_hard, 'ver_soft': onu_ver_soft, 'desc': onu_desc, 'volt': onu_volt, 'temp': onu_temp })     


        #UserIp
        PortIp = []
    
        port_ip = os.popen('snmpwalk -v2c -c ' + community + ' ' + ip + ' iso.3.6.1.4.1.34592.1.3.100.5.4.1.3')
        for ip in port_ip:
            IpVlan = ip.split('=')[0].split('.')
            PortIp.append({'user_mac': ip.split('=')[1].split(':')[-1].strip().replace(' ', ':'),
            'ip': IpVlan[-5] +'.'+IpVlan[-4] +'.'+ IpVlan[-3]+'.'+IpVlan[-2]+'('+IpVlan[-1].strip()+')'})          

        try:
            for mac in onu_user_mac:
                for ips in PortIp:
                    if mac['user_mac'] in ips['user_mac']:    
                        all[0]['mac_ip'].append({'port': mac['user_port'], 'ip': ips['ip'], 'mac': ips['user_mac'],'type': 'd'})         
           
            if len(all[0]['mac_ip']) == 0:
                for mac in onu_user_mac:
                    all[0]['mac_ip'].append({'port': mac['user_port'], 'mac': mac['user_mac'],'type': 's'})
        except:
            pass

        return all                              
             

    def onu_reboot(self, ip, community_rw, OnuId):
        Reboot = os.popen('snmpset -v2c -c ' + community_rw + ' ' + ip + ' .1.3.6.1.4.1.17409.2.3.4.1.1.17.' + OnuId + ' i' + ' 1')
        for r_reboot in Reboot:
            return r_reboot.split('=')[1].split(':')[-1].strip()

    def onu_delete(self, ip, community_rw, OnuId):
        Delete = os.popen('snmpset -v2c -c ' + community_rw + ' ' + ip + ' .1.3.6.1.4.1.17409.2.3.4.5.2.1.4.' + OnuId + ' i' + ' 6')
        for r_delete in Delete:
            return r_delete.split('=')[1].split(':')[-1].strip()

