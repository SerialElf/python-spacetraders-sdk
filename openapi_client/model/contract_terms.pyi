# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.     # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ContractTerms(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "payment",
            "deadline",
        }
        
        class properties:
            deadline = schemas.DateTimeSchema
        
            @staticmethod
            def payment() -> typing.Type['ContractPayment']:
                return ContractPayment
            
            
            class deliver(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContractDeliverGood']:
                        return ContractDeliverGood
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ContractDeliverGood'], typing.List['ContractDeliverGood']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deliver':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContractDeliverGood':
                    return super().__getitem__(i)
            __annotations__ = {
                "deadline": deadline,
                "payment": payment,
                "deliver": deliver,
            }
    
    payment: 'ContractPayment'
    deadline: MetaOapg.properties.deadline
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deadline"]) -> MetaOapg.properties.deadline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> 'ContractPayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver"]) -> MetaOapg.properties.deliver: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["deadline", "payment", "deliver", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deadline"]) -> MetaOapg.properties.deadline: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> 'ContractPayment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver"]) -> typing.Union[MetaOapg.properties.deliver, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deadline", "payment", "deliver", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        payment: 'ContractPayment',
        deadline: typing.Union[MetaOapg.properties.deadline, str, datetime, ],
        deliver: typing.Union[MetaOapg.properties.deliver, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractTerms':
        return super().__new__(
            cls,
            *_args,
            payment=payment,
            deadline=deadline,
            deliver=deliver,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.contract_deliver_good import ContractDeliverGood
from openapi_client.model.contract_payment import ContractPayment
