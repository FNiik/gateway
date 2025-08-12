import graphene
from graphene_django import DjangoObjectType
from .models import Gateway
from django.core.paginator import Paginator

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


# for quering the gateway        
class Query(graphene.ObjectType):
    paginated_gateways= graphene.Field(#return object of paginatedGatewayType
        paginatedGatewayType,
        page=graphene.Int(required=False, default_value=1),
        page_size=graphene.Int(required=False, default_value=3),
    )
    gateways_list= graphene.List(GatewayType)
    gateway= graphene.Field(GatewayType, id=graphene.ID(required=True))    
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


class Mutation(graphene.ObjectType):
    createGateway= CreateGateway.Field()
    updateGateway= UpdateGateway.Field()
    deleteGateway= DeleteGateway.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)        