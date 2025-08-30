import grpc
from . import gatewayagent_pb2 as pb2
from . import gatewayagent_pb2_grpc as pb2_grp





def net_adapter_info():
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        return stub.NetAdapterInfo(pb2.NullRequest())
       
def set_date_time(new_date,new_time):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        set_date_time_request=pb2.SetDateTimeRequest(new_date=new_date,new_time=new_time)
        return stub.SetDateTime(set_date_time_request)
        
    
def get_date_time():
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        return stub.GetDateTime(pb2.NullRequest())
def add_route(destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        destination_interface=pb2.GeneralEthernetCardInfo(
            index=destination_index,
            ip=destination_ip,
            mask=destination_mask,
            gateway=destination_gateway
        )
        route_info=pb2.RouteInfo(
            destination_interface=destination_interface,
            gateway_ip=gateway_ip,
            metric=metric,
            interface_name=interface_name,
            interface_index=interface_index
        )
        return stub.AddRoute(route_info)
def remove_route(destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        destination_interface=pb2.GeneralEthernetCardInfo(
            index=destination_index,
            ip=destination_ip,
            mask=destination_mask,
            gateway=destination_gateway
        )
        route_info=pb2.RouteInfo(
            destination_interface=destination_interface,
            gateway_ip=gateway_ip,
            metric=metric,
            interface_name=interface_name,
            interface_index=interface_index
        )
        return stub.RemoveRoute(route_info)
def show_route():
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        return stub.ShowRoute(pb2.NullRequest())
def arp():
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        return stub.Arp(pb2.NullRequest())

def ping(ip):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        ping_request=pb2.PingRequest(ip=ip)
        return stub.Ping(ping_request)
def trace_route(ip):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        trace_route_request=pb2.TraceRouteRequest(ip=ip)
        return stub.TraceRoute(trace_route_request)
def tcp_port_test(ip, port):
    with grpc.insecure_channel('192.168.117.131:2425') as channel:
        stub=pb2_grp.GatewayAgentStub(channel)
        tcp_port_test_request=pb2.TcpPortTestRequest(ip=ip, port=port)
        return stub.TcpPortTest(tcp_port_test_request)
    


                






        
        
           
        



        
