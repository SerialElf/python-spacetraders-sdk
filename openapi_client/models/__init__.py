# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.agent import Agent
from openapi_client.model.chart import Chart
from openapi_client.model.connected_system import ConnectedSystem
from openapi_client.model.contract import Contract
from openapi_client.model.contract_deliver_good import ContractDeliverGood
from openapi_client.model.contract_payment import ContractPayment
from openapi_client.model.contract_terms import ContractTerms
from openapi_client.model.cooldown import Cooldown
from openapi_client.model.extraction import Extraction
from openapi_client.model.extraction_yield import ExtractionYield
from openapi_client.model.faction import Faction
from openapi_client.model.faction_trait import FactionTrait
from openapi_client.model.jump_gate import JumpGate
from openapi_client.model.market import Market
from openapi_client.model.market_trade_good import MarketTradeGood
from openapi_client.model.market_transaction import MarketTransaction
from openapi_client.model.meta import Meta
from openapi_client.model.scanned_ship import ScannedShip
from openapi_client.model.scanned_system import ScannedSystem
from openapi_client.model.scanned_waypoint import ScannedWaypoint
from openapi_client.model.ship import Ship
from openapi_client.model.ship_cargo import ShipCargo
from openapi_client.model.ship_cargo_item import ShipCargoItem
from openapi_client.model.ship_condition import ShipCondition
from openapi_client.model.ship_crew import ShipCrew
from openapi_client.model.ship_engine import ShipEngine
from openapi_client.model.ship_frame import ShipFrame
from openapi_client.model.ship_fuel import ShipFuel
from openapi_client.model.ship_module import ShipModule
from openapi_client.model.ship_mount import ShipMount
from openapi_client.model.ship_nav import ShipNav
from openapi_client.model.ship_nav_flight_mode import ShipNavFlightMode
from openapi_client.model.ship_nav_route import ShipNavRoute
from openapi_client.model.ship_nav_route_waypoint import ShipNavRouteWaypoint
from openapi_client.model.ship_nav_status import ShipNavStatus
from openapi_client.model.ship_reactor import ShipReactor
from openapi_client.model.ship_registration import ShipRegistration
from openapi_client.model.ship_requirements import ShipRequirements
from openapi_client.model.ship_role import ShipRole
from openapi_client.model.ship_type import ShipType
from openapi_client.model.shipyard import Shipyard
from openapi_client.model.shipyard_ship import ShipyardShip
from openapi_client.model.shipyard_transaction import ShipyardTransaction
from openapi_client.model.survey import Survey
from openapi_client.model.survey_deposit import SurveyDeposit
from openapi_client.model.system import System
from openapi_client.model.system_faction import SystemFaction
from openapi_client.model.system_type import SystemType
from openapi_client.model.system_waypoint import SystemWaypoint
from openapi_client.model.trade_good import TradeGood
from openapi_client.model.trade_symbol import TradeSymbol
from openapi_client.model.waypoint import Waypoint
from openapi_client.model.waypoint_faction import WaypointFaction
from openapi_client.model.waypoint_orbital import WaypointOrbital
from openapi_client.model.waypoint_trait import WaypointTrait
from openapi_client.model.waypoint_type import WaypointType
