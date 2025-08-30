import graphene
from graphene_django import DjangoObjectType
from .models import Gateway
from django.core.paginator import Paginator
from . import grpc_functions

# Update the resolve_paginated_gateways method to fetch only the required gateways for the page

# importing the Gaateway model for creating the schema
class GatewayType(DjangoObjectType):
    class Meta:
        model= Gateway
        fields= "__all__"
class paginatedGatewayType(graphene.ObjectType):
    gateways= graphene.List(GatewayType)
    total_count= graphene.Int()
    page= graphene.Int()
    page_size= graphene.Int()
    has_next= graphene.Boolean()
    has_previous= graphene.Boolean()
class NetworkAddressType(graphene.ObjectType):
    ip=graphene.String()
    mask=graphene.String()
class IpSetModeType(graphene.Enum):
    DHCP = 0
    MANUAL = 1
    
class NetAdapterInfoType(graphene.ObjectType):
    index=graphene.Int()
    name=graphene.String()
    description=graphene.String()
    address=graphene.List(NetworkAddressType)
    gateway=graphene.String()
    ip_set_mode=IpSetModeType()
    activity=graphene.Boolean()
    enability=graphene.Boolean()
class NetAdapterInfoResponseType(graphene.ObjectType):
    all_net_adapters_info=graphene.String()
    net_adapter_info=graphene.List(NetAdapterInfoType)
class GetDateTimeType(graphene.ObjectType):
    current_date=graphene.String()
    current_time=graphene.String()
class GeneralEthernetCardInfo(graphene.ObjectType):
    index=graphene.Int()
    ip=graphene.String()
    mask=graphene.String()
    gateway=graphene.String()
class RouteInfoType(graphene.ObjectType):
    destination_interface=graphene.Field(GeneralEthernetCardInfo)
    gateway_ip=graphene.String()
    metric=graphene.Int()
    interface_name=graphene.String()
    interface_index=graphene.Int()    
class ShowRoutesResponseType(graphene.ObjectType):
    all_route_info=graphene.String()
    route_info=graphene.List(RouteInfoType) 

class ExecutionResponseType(graphene.ObjectType):
    response=graphene.String()

    
class Query(graphene.ObjectType):
    paginated_gateways= graphene.Field(#return object of paginatedGatewayType
        paginatedGatewayType,
        page=graphene.Int(required=False, default_value=1),
        page_size=graphene.Int(required=False, default_value=3),
    )
    gateways_list= graphene.List(GatewayType)
    gateway= graphene.Field(GatewayType, id=graphene.ID(required=True)) 
    net_adapter_info=graphene.Field(NetAdapterInfoResponseType)
    # set_date_time=graphene.Field(graphene.String, new_date=graphene.String(required=True), new_time=graphene.String(required=True))
    get_date_time=graphene.Field(GetDateTimeType)
    # add_route=graphene.Field(graphene.String(), destination_index=graphene.Int(required=True), destination_ip=graphene.)
    show_route=graphene.Field(ShowRoutesResponseType)
    arp=graphene.Field(ExecutionResponseType)



    def resolve_gateways_list(self, info):
        return Gateway.objects.all()
    def resolve_gateway(self, info, id):
        try:
            return Gateway.objects.get(pk=id)
        except Gateway.DoesNotExist:
            return (False, "gateway not found")
    def resolve_paginated_gateways(self, info, page, page_size):
        
        paginator = Paginator(Gateway.objects.all(), page_size)
        paginated_gateways = paginator.get_page(page)
        has_next = paginated_gateways.has_next()
        has_previous = paginated_gateways.has_previous()
        total_count = paginator.count

        return paginatedGatewayType(
            gateways=paginated_gateways.object_list,
            total_count=total_count,
            page=page,
            page_size=page_size,
            has_next=has_next,
            has_previous=has_previous,
        )
    def resolve_net_adapter_info(self, info):
        response=grpc_functions.net_adapter_info()
        if response:
            net_adapter_info_list = []
            for adapter in response.net_adapter_info:  #because this is list
                address_list = []
                for address in adapter.addresses:
                    address_list.append(NetworkAddressType(ip=address.ip, mask=address.mask))
                net_adapter_info_list.append(
                    NetAdapterInfoType(
                        index=adapter.index,
                        name=adapter.name,
                        description=adapter.description,
                        address=address_list,
                        gateway=adapter.gateway,
                        ip_set_mode=adapter.ip_set_mode,
                        activity=adapter.activity,
                        enability=adapter.enability



                    )

                )    
        return NetAdapterInfoResponseType(
            all_net_adapters_info=response.all_net_adapters_info,
            net_adapter_info=net_adapter_info_list
        )
    def resolve_show_route(self, info):
        response=grpc_functions.show_route()
        if response:
            route_info_list=[]
            
            for route_info in response.route_info:
                destination_interface=GeneralEthernetCardInfo(
                    index=route_info.destination_interface.index,
                    ip=route_info.destination_interface.ip,
                    mask=route_info.destination_interface.mask,
                    gateway=route_info.destination_interface.gateway
                    )
                route_info_list.append(RouteInfoType(
                    destination_interface=destination_interface,
                    gateway_ip=route_info.gateway_ip,
                    metric=route_info.metric,
                    interface_name=route_info.interface_name,
                    interface_index=route_info.interface_index



                ))
            return ShowRoutesResponseType(
                all_route_info=response.all_route_info,
                route_info=route_info_list

            )   
    def resolve_arp(self, info):
        resive=grpc_functions.arp()
        if resive:
            return ExecutionResponseType(
                response=resive.response
            )

                                                
                

                


# def resolve_set_date_time(self, info, new_date, new_time):
#     response=grpc_functions.set_date_time(new_date, new_time)
#     if response:
#         return(f"Date and time successfully updated to {new_date}   {new_time}") 
#     else:
#         return "Failed to update date and time"

# def resolve_get_date_time(self, info):
#     response=grpc_functions.get_date_time()
#     if response:
#         return GetDateTimeType(
#             current_date=response.current_date,
#             current_time= response.cuurent_time
#         )
    
    



class CreateGateway(graphene.Mutation):
    class Arguments:
        name= graphene.String(required=True)
        ip_address= graphene.String(required=True)
        port_number= graphene.Int(required=True)
        description= graphene.String(required=False)
        io= graphene.String(required=False)
        status= graphene.String(required=False)
        location = graphene.String(required=False)
    gateway= graphene.Field(GatewayType)  
    ok = graphene.Boolean()  
    def mutate(self, info, name, ip_address, port_number, description=None, io=None , status=None, location=None):
        gateway= Gateway(
            name=name,
            ip_address=ip_address,
            port_number=port_number,
            description=description,
            io=io,
            status=status,
            location=location

        )
        gateway.save()
        ok= True
        return CreateGateway(gateway=gateway, ok=ok)
#for updating the gateway    
class UpdateGateway(graphene.Mutation):

    class Arguments:
        id= graphene.ID(required=True)
        name= graphene.String(required=False)
        ip_address= graphene.String(required=False)
        port_number= graphene.Int(required=False)
        description= graphene.String(required=False)
        io= graphene.String(required=False)
        status= graphene.String(required=False)
        location = graphene.String(required=False)
    gateway= graphene.Field(GatewayType)  
    ok = graphene.Boolean()
    message= graphene.String() 
    def mutate(self, info, id, name=None, ip_address=None, port_number=None, description=None, io=None, status=None, location=None):
        try:
            gateway= Gateway.objects.get(pk=id)
            if name is not None:
                gateway.name= name
            if ip_address is not None:
                gateway.ip_address=ip_address
            if port_number is not None:
                gateway.port_number=port_number

            if description is not None:
                gateway.description=description
            if io is not None:
                gateway.io=io
            if status is not None:
                gateway.status=status
            if location is not None:
                gateway.location=location        

            gateway.save()
            ok=True
            message="Gateway updated successfully"
        except Gateway.DoesNotExist:
            ok=False
            gateway=None
            message="Gateway not found"
        return UpdateGateway(gateway=gateway, ok=ok, message=message)


class DeleteGateway(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, id):
        try:
            gateway=Gateway.objects.get(pk=id)
            gateway.delete()
            ok=True
            message="Gateway deleted successfully"
        except Gateway.DoesNotExist:
            ok=False
            message="Gateway not found"
            #gateway=None
        return DeleteGateway(ok=ok, message=message)                    

class set_date_time(graphene.Mutation):
    class Arguments:
        new_date=graphene.String(required=True)
        new_time=graphene.String(required=True)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, new_date, new_time):
        try:
            response=grpc_functions.set_date_time(new_date, new_time)
            ok=True
            message="New date and time set"
        except Exception as e:
            ok=False
            message=" Set new date and time failed\n {}".format(e)
        return set_date_time(ok=ok, message=message)    
class add_route(graphene.Mutation):
    class Arguments:
        destination_index=graphene.Int(required=True)
        destination_ip=graphene.String(required=True)
        destination_mask=graphene.String(required=True)
        destination_gateway=graphene.String(required=True)
        gateway_ip=graphene.String(required=True)
        metric=graphene.Int(required=True)
        interface_name=graphene.String(required=True)
        interface_index=graphene.Int(required=True)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index):
        try:
            response=grpc_functions.add_route(destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index)
            ok=True
            message="New route added"
        except Exception as e:
            ok=False
            message="Add new route failed \n {}".format(e)    
        return add_route(ok=ok, message=message)
    
class remove_route(graphene.Mutation):
    class Arguments:
        destination_index=graphene.Int(required=True)
        destination_ip=graphene.String(required=True)
        destination_mask=graphene.String(required=True)
        destination_gateway=graphene.String(required=True)
        gateway_ip=graphene.String(required=True)
        metric=graphene.Int(required=True)
        interface_name=graphene.String(required=True)
        interface_index=graphene.Int(required=True)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index):
        try:
            response=grpc_functions.remove_route(destination_index, destination_ip, destination_mask, destination_gateway, gateway_ip, metric, interface_name, interface_index)
            ok=True
            message=" Route removed"
        except Exception as e:
            ok=False
            message="Remove route failed \n {}".format(e)    
        return remove_route(ok=ok, message=message)
    

class ping(graphene.Mutation):
    class Arguments:
        ip=graphene.String(required=True)
    response=graphene.Field(ExecutionResponseType)
    ok=graphene.Boolean()
    message= graphene.String()

    def mutate(self, info, ip):
        try:
            grpc_response=grpc_functions.ping(ip)
            response = ExecutionResponseType(response=grpc_response.response)
            ok=True
            message="ping run"
        except Exception as e:
            ok=False
            message="ping failed\n {}".format(e)
            response=None
        return ping(response=response, ok=ok, message=message)        
            

class trace_route(graphene.Mutation):
    class Arguments:
        ip=graphene.String(required=True)
    response=graphene.Field(ExecutionResponseType)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, ip):
        try:
            grpc_response=grpc_functions.trace_route(ip)
            response = ExecutionResponseType(response=grpc_response.response)
            ok=True
            message="tcp route run"
        
        except Exception as e:
            ok=False
            message="trace route failed\n {}".format(e)
            response=None
        return trace_route(response=response, ok=ok, message=message)  
    

class tcp_port_test(graphene.Mutation):
    class Arguments:
        ip=graphene.String(required=True)
        port=graphene.Int(required=True)
    response=graphene.Field(ExecutionResponseType)
    ok=graphene.Boolean()
    message= graphene.String()
    def mutate(self, info, ip, port):
        try:
            grpc_response=grpc_functions.tcp_port_test(ip, port)
            response = ExecutionResponseType(response=grpc_response.response)
            ok=True
            message="tcp port test run"
        except Exception as e:
            response=None
            ok=False
            message="tcp port test failed \n {}".format(e)
        return tcp_port_test(response=response, ok=ok, message=message)    

                


        








            

        # response=grpc_functions.set_date_time(new_date, new_time)
        
        #     ok=True
        #     message="New date and time set"    
        # else:
        #     ok=False
        #     message=" Set new date and time failed"    
        # return set_date_time(ok=ok, message=message)    

class Mutation(graphene.ObjectType):
    createGateway= CreateGateway.Field()
    updateGateway= UpdateGateway.Field()
    deleteGateway= DeleteGateway.Field()
    Set_date_time= set_date_time.Field()
    Add_route= add_route.Field()
    Remove_route= remove_route.Field()
    Ping=ping.Field() 
    Trace_route=trace_route.Field()
    Tcp_port_test=tcp_port_test.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)        