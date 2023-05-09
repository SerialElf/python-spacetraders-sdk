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


class SystemType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of waypoint.
    """


    class MetaOapg:
        enum_value_to_name = {
            "NEUTRON_STAR": "NEUTRON_STAR",
            "RED_STAR": "RED_STAR",
            "ORANGE_STAR": "ORANGE_STAR",
            "BLUE_STAR": "BLUE_STAR",
            "YOUNG_STAR": "YOUNG_STAR",
            "WHITE_DWARF": "WHITE_DWARF",
            "BLACK_HOLE": "BLACK_HOLE",
            "HYPERGIANT": "HYPERGIANT",
            "NEBULA": "NEBULA",
            "UNSTABLE": "UNSTABLE",
        }
    
    @schemas.classproperty
    def NEUTRON_STAR(cls):
        return cls("NEUTRON_STAR")
    
    @schemas.classproperty
    def RED_STAR(cls):
        return cls("RED_STAR")
    
    @schemas.classproperty
    def ORANGE_STAR(cls):
        return cls("ORANGE_STAR")
    
    @schemas.classproperty
    def BLUE_STAR(cls):
        return cls("BLUE_STAR")
    
    @schemas.classproperty
    def YOUNG_STAR(cls):
        return cls("YOUNG_STAR")
    
    @schemas.classproperty
    def WHITE_DWARF(cls):
        return cls("WHITE_DWARF")
    
    @schemas.classproperty
    def BLACK_HOLE(cls):
        return cls("BLACK_HOLE")
    
    @schemas.classproperty
    def HYPERGIANT(cls):
        return cls("HYPERGIANT")
    
    @schemas.classproperty
    def NEBULA(cls):
        return cls("NEBULA")
    
    @schemas.classproperty
    def UNSTABLE(cls):
        return cls("UNSTABLE")
