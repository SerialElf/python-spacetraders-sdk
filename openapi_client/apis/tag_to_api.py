import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.factions_api import FactionsApi
from openapi_client.apis.tags.fleet_api import FleetApi
from openapi_client.apis.tags.contracts_api import ContractsApi
from openapi_client.apis.tags.systems_api import SystemsApi
from openapi_client.apis.tags.agents_api import AgentsApi
from openapi_client.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
