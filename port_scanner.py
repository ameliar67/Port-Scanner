import socket
import common_ports as common_ports

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    dict_ports = common_ports.ports_and_services
  

    port_range = range(port_range[0], port_range[1] + 1)
    count = 0

    final = ''

    def hostname_ip_retreiver(port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(3)
        
      try:
        if s.connect_ex((target, port)):
          #print(s.connect_ex((target, port)), target, port, 'cannot connect')
          s.close()
        else:

          ip_address = socket.gethostbyaddr(target)
          print(ip_address, 'ip')
          s.close()
          return ip_address

          
      except:
          s.close()
      

  
    def portScanner(port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(3)
        
      try:
        if s.connect_ex((target, port)):
          #print(s.connect_ex((target, port)), target, port, 'cannot connect')
          s.close()
        else:
          s.close()
          return port

      except:
          s.close()

  

    for port in port_range:
          
      hello = portScanner(port)  
     
      if hello == None:
        continue
        
      else:

        if verbose == False:
          open_ports.append(hello)
          
        elif count == 0 and verbose is True:
          returned_info = hostname_ip_retreiver(port)
          
          if returned_info == None:
            final = '''Open ports for ''' + target + '''
PORT     SERVICE'''

            if hello > 99:
              final = final + '''
''' + str(hello) + '''      ''' + dict_ports[hello]
            else:
              final = final + '''
''' + str(hello) + '''       ''' + dict_ports[hello]
            
          else:
            final = '''Open ports for ''' + returned_info[0] + ''' (''' + returned_info[2][0] + ''')
PORT     SERVICE'''

            if hello > 99:
              final = final + '''
''' + str(hello) + '''      ''' + dict_ports[hello]
            else:
              final = final + '''
''' + str(hello) + '''       ''' + dict_ports[hello]
        
        else:
            
          final = final + '''
''' + str(hello) + '''       ''' + dict_ports[hello]
          
        count = count + 1
  
    if verbose is True:
  
      open_ports = final
        
    if open_ports == []:
      if target.find('e') != -1:
        open_ports = 'Error: Invalid hostname'
      else: 
        open_ports = 'Error: Invalid IP address'

  

    return(open_ports)

    