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


class TradeSymbol(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def PRECIOUS_STONES(cls):
        return cls("PRECIOUS_STONES")
    
    @schemas.classproperty
    def QUARTZ_SAND(cls):
        return cls("QUARTZ_SAND")
    
    @schemas.classproperty
    def SILICON_CRYSTALS(cls):
        return cls("SILICON_CRYSTALS")
    
    @schemas.classproperty
    def AMMONIA_ICE(cls):
        return cls("AMMONIA_ICE")
    
    @schemas.classproperty
    def LIQUID_HYDROGEN(cls):
        return cls("LIQUID_HYDROGEN")
    
    @schemas.classproperty
    def LIQUID_NITROGEN(cls):
        return cls("LIQUID_NITROGEN")
    
    @schemas.classproperty
    def ICE_WATER(cls):
        return cls("ICE_WATER")
    
    @schemas.classproperty
    def EXOTIC_MATTER(cls):
        return cls("EXOTIC_MATTER")
    
    @schemas.classproperty
    def ADVANCED_CIRCUITRY(cls):
        return cls("ADVANCED_CIRCUITRY")
    
    @schemas.classproperty
    def GRAVITON_EMITTERS(cls):
        return cls("GRAVITON_EMITTERS")
    
    @schemas.classproperty
    def IRON(cls):
        return cls("IRON")
    
    @schemas.classproperty
    def IRON_ORE(cls):
        return cls("IRON_ORE")
    
    @schemas.classproperty
    def COPPER(cls):
        return cls("COPPER")
    
    @schemas.classproperty
    def COPPER_ORE(cls):
        return cls("COPPER_ORE")
    
    @schemas.classproperty
    def ALUMINUM(cls):
        return cls("ALUMINUM")
    
    @schemas.classproperty
    def ALUMINUM_ORE(cls):
        return cls("ALUMINUM_ORE")
    
    @schemas.classproperty
    def SILVER(cls):
        return cls("SILVER")
    
    @schemas.classproperty
    def SILVER_ORE(cls):
        return cls("SILVER_ORE")
    
    @schemas.classproperty
    def GOLD(cls):
        return cls("GOLD")
    
    @schemas.classproperty
    def GOLD_ORE(cls):
        return cls("GOLD_ORE")
    
    @schemas.classproperty
    def PLATINUM(cls):
        return cls("PLATINUM")
    
    @schemas.classproperty
    def PLATINUM_ORE(cls):
        return cls("PLATINUM_ORE")
    
    @schemas.classproperty
    def DIAMONDS(cls):
        return cls("DIAMONDS")
    
    @schemas.classproperty
    def URANITE(cls):
        return cls("URANITE")
    
    @schemas.classproperty
    def URANITE_ORE(cls):
        return cls("URANITE_ORE")
    
    @schemas.classproperty
    def MERITIUM(cls):
        return cls("MERITIUM")
    
    @schemas.classproperty
    def MERITIUM_ORE(cls):
        return cls("MERITIUM_ORE")
    
    @schemas.classproperty
    def HYDROCARBON(cls):
        return cls("HYDROCARBON")
    
    @schemas.classproperty
    def ANTIMATTER(cls):
        return cls("ANTIMATTER")
    
    @schemas.classproperty
    def FERTILIZERS(cls):
        return cls("FERTILIZERS")
    
    @schemas.classproperty
    def FABRICS(cls):
        return cls("FABRICS")
    
    @schemas.classproperty
    def FOOD(cls):
        return cls("FOOD")
    
    @schemas.classproperty
    def JEWELRY(cls):
        return cls("JEWELRY")
    
    @schemas.classproperty
    def MACHINERY(cls):
        return cls("MACHINERY")
    
    @schemas.classproperty
    def FIREARMS(cls):
        return cls("FIREARMS")
    
    @schemas.classproperty
    def ASSAULT_RIFLES(cls):
        return cls("ASSAULT_RIFLES")
    
    @schemas.classproperty
    def MILITARY_EQUIPMENT(cls):
        return cls("MILITARY_EQUIPMENT")
    
    @schemas.classproperty
    def EXPLOSIVES(cls):
        return cls("EXPLOSIVES")
    
    @schemas.classproperty
    def LAB_INSTRUMENTS(cls):
        return cls("LAB_INSTRUMENTS")
    
    @schemas.classproperty
    def AMMUNITION(cls):
        return cls("AMMUNITION")
    
    @schemas.classproperty
    def ELECTRONICS(cls):
        return cls("ELECTRONICS")
    
    @schemas.classproperty
    def SHIP_PLATING(cls):
        return cls("SHIP_PLATING")
    
    @schemas.classproperty
    def EQUIPMENT(cls):
        return cls("EQUIPMENT")
    
    @schemas.classproperty
    def FUEL(cls):
        return cls("FUEL")
    
    @schemas.classproperty
    def MEDICINE(cls):
        return cls("MEDICINE")
    
    @schemas.classproperty
    def DRUGS(cls):
        return cls("DRUGS")
    
    @schemas.classproperty
    def CLOTHING(cls):
        return cls("CLOTHING")
    
    @schemas.classproperty
    def MICROPROCESSORS(cls):
        return cls("MICROPROCESSORS")
    
    @schemas.classproperty
    def PLASTICS(cls):
        return cls("PLASTICS")
    
    @schemas.classproperty
    def POLYNUCLEOTIDES(cls):
        return cls("POLYNUCLEOTIDES")
    
    @schemas.classproperty
    def BIOCOMPOSITES(cls):
        return cls("BIOCOMPOSITES")
    
    @schemas.classproperty
    def NANOBOTS(cls):
        return cls("NANOBOTS")
    
    @schemas.classproperty
    def AI_MAINFRAMES(cls):
        return cls("AI_MAINFRAMES")
    
    @schemas.classproperty
    def QUANTUM_DRIVES(cls):
        return cls("QUANTUM_DRIVES")
    
    @schemas.classproperty
    def ROBOTIC_DRONES(cls):
        return cls("ROBOTIC_DRONES")
    
    @schemas.classproperty
    def CYBER_IMPLANTS(cls):
        return cls("CYBER_IMPLANTS")
    
    @schemas.classproperty
    def GENE_THERAPEUTICS(cls):
        return cls("GENE_THERAPEUTICS")
    
    @schemas.classproperty
    def NEURAL_CHIPS(cls):
        return cls("NEURAL_CHIPS")
    
    @schemas.classproperty
    def MOOD_REGULATORS(cls):
        return cls("MOOD_REGULATORS")
    
    @schemas.classproperty
    def VIRAL_AGENTS(cls):
        return cls("VIRAL_AGENTS")
    
    @schemas.classproperty
    def MICRO_FUSION_GENERATORS(cls):
        return cls("MICRO_FUSION_GENERATORS")
    
    @schemas.classproperty
    def SUPERGRAINS(cls):
        return cls("SUPERGRAINS")
    
    @schemas.classproperty
    def LASER_RIFLES(cls):
        return cls("LASER_RIFLES")
    
    @schemas.classproperty
    def HOLOGRAPHICS(cls):
        return cls("HOLOGRAPHICS")
    
    @schemas.classproperty
    def SHIP_SALVAGE(cls):
        return cls("SHIP_SALVAGE")
    
    @schemas.classproperty
    def RELIC_TECH(cls):
        return cls("RELIC_TECH")
    
    @schemas.classproperty
    def NOVEL_LIFEFORMS(cls):
        return cls("NOVEL_LIFEFORMS")
    
    @schemas.classproperty
    def BOTANICAL_SPECIMENS(cls):
        return cls("BOTANICAL_SPECIMENS")
    
    @schemas.classproperty
    def CULTURAL_ARTIFACTS(cls):
        return cls("CULTURAL_ARTIFACTS")
    
    @schemas.classproperty
    def REACTOR_SOLAR_I(cls):
        return cls("REACTOR_SOLAR_I")
    
    @schemas.classproperty
    def REACTOR_FUSION_I(cls):
        return cls("REACTOR_FUSION_I")
    
    @schemas.classproperty
    def REACTOR_FISSION_I(cls):
        return cls("REACTOR_FISSION_I")
    
    @schemas.classproperty
    def REACTOR_CHEMICAL_I(cls):
        return cls("REACTOR_CHEMICAL_I")
    
    @schemas.classproperty
    def REACTOR_ANTIMATTER_I(cls):
        return cls("REACTOR_ANTIMATTER_I")
    
    @schemas.classproperty
    def ENGINE_IMPULSE_DRIVE_I(cls):
        return cls("ENGINE_IMPULSE_DRIVE_I")
    
    @schemas.classproperty
    def ENGINE_ION_DRIVE_I(cls):
        return cls("ENGINE_ION_DRIVE_I")
    
    @schemas.classproperty
    def ENGINE_ION_DRIVE_II(cls):
        return cls("ENGINE_ION_DRIVE_II")
    
    @schemas.classproperty
    def ENGINE_HYPER_DRIVE_I(cls):
        return cls("ENGINE_HYPER_DRIVE_I")
    
    @schemas.classproperty
    def MODULE_MINERAL_PROCESSOR_I(cls):
        return cls("MODULE_MINERAL_PROCESSOR_I")
    
    @schemas.classproperty
    def MODULE_CARGO_HOLD_I(cls):
        return cls("MODULE_CARGO_HOLD_I")
    
    @schemas.classproperty
    def MODULE_CREW_QUARTERS_I(cls):
        return cls("MODULE_CREW_QUARTERS_I")
    
    @schemas.classproperty
    def MODULE_ENVOY_QUARTERS_I(cls):
        return cls("MODULE_ENVOY_QUARTERS_I")
    
    @schemas.classproperty
    def MODULE_PASSENGER_CABIN_I(cls):
        return cls("MODULE_PASSENGER_CABIN_I")
    
    @schemas.classproperty
    def MODULE_MICRO_REFINERY_I(cls):
        return cls("MODULE_MICRO_REFINERY_I")
    
    @schemas.classproperty
    def MODULE_ORE_REFINERY_I(cls):
        return cls("MODULE_ORE_REFINERY_I")
    
    @schemas.classproperty
    def MODULE_FUEL_REFINERY_I(cls):
        return cls("MODULE_FUEL_REFINERY_I")
    
    @schemas.classproperty
    def MODULE_SCIENCE_LAB_I(cls):
        return cls("MODULE_SCIENCE_LAB_I")
    
    @schemas.classproperty
    def MODULE_JUMP_DRIVE_I(cls):
        return cls("MODULE_JUMP_DRIVE_I")
    
    @schemas.classproperty
    def MODULE_JUMP_DRIVE_II(cls):
        return cls("MODULE_JUMP_DRIVE_II")
    
    @schemas.classproperty
    def MODULE_JUMP_DRIVE_III(cls):
        return cls("MODULE_JUMP_DRIVE_III")
    
    @schemas.classproperty
    def MODULE_WARP_DRIVE_I(cls):
        return cls("MODULE_WARP_DRIVE_I")
    
    @schemas.classproperty
    def MODULE_WARP_DRIVE_II(cls):
        return cls("MODULE_WARP_DRIVE_II")
    
    @schemas.classproperty
    def MODULE_WARP_DRIVE_III(cls):
        return cls("MODULE_WARP_DRIVE_III")
    
    @schemas.classproperty
    def MODULE_SHIELD_GENERATOR_I(cls):
        return cls("MODULE_SHIELD_GENERATOR_I")
    
    @schemas.classproperty
    def MODULE_SHIELD_GENERATOR_II(cls):
        return cls("MODULE_SHIELD_GENERATOR_II")
    
    @schemas.classproperty
    def MOUNT_GAS_SIPHON_I(cls):
        return cls("MOUNT_GAS_SIPHON_I")
    
    @schemas.classproperty
    def MOUNT_GAS_SIPHON_II(cls):
        return cls("MOUNT_GAS_SIPHON_II")
    
    @schemas.classproperty
    def MOUNT_GAS_SIPHON_III(cls):
        return cls("MOUNT_GAS_SIPHON_III")
    
    @schemas.classproperty
    def MOUNT_SURVEYOR_I(cls):
        return cls("MOUNT_SURVEYOR_I")
    
    @schemas.classproperty
    def MOUNT_SURVEYOR_II(cls):
        return cls("MOUNT_SURVEYOR_II")
    
    @schemas.classproperty
    def MOUNT_SURVEYOR_III(cls):
        return cls("MOUNT_SURVEYOR_III")
    
    @schemas.classproperty
    def MOUNT_SENSOR_ARRAY_I(cls):
        return cls("MOUNT_SENSOR_ARRAY_I")
    
    @schemas.classproperty
    def MOUNT_SENSOR_ARRAY_II(cls):
        return cls("MOUNT_SENSOR_ARRAY_II")
    
    @schemas.classproperty
    def MOUNT_SENSOR_ARRAY_III(cls):
        return cls("MOUNT_SENSOR_ARRAY_III")
    
    @schemas.classproperty
    def MOUNT_MINING_LASER_I(cls):
        return cls("MOUNT_MINING_LASER_I")
    
    @schemas.classproperty
    def MOUNT_MINING_LASER_II(cls):
        return cls("MOUNT_MINING_LASER_II")
    
    @schemas.classproperty
    def MOUNT_MINING_LASER_III(cls):
        return cls("MOUNT_MINING_LASER_III")
    
    @schemas.classproperty
    def MOUNT_LASER_CANNON_I(cls):
        return cls("MOUNT_LASER_CANNON_I")
    
    @schemas.classproperty
    def MOUNT_MISSILE_LAUNCHER_I(cls):
        return cls("MOUNT_MISSILE_LAUNCHER_I")
    
    @schemas.classproperty
    def MOUNT_TURRET_I(cls):
        return cls("MOUNT_TURRET_I")
