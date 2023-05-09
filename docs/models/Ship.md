# openapi_client.model.ship.Ship

A ship

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A ship | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The globally unique identifier of the ship in the following format: &#x60;[AGENT_SYMBOL]_[HEX_ID]&#x60; | 
**nav** | [**ShipNav**](ShipNav.md) | [**ShipNav**](ShipNav.md) |  | 
**engine** | [**ShipEngine**](ShipEngine.md) | [**ShipEngine**](ShipEngine.md) |  | 
**fuel** | [**ShipFuel**](ShipFuel.md) | [**ShipFuel**](ShipFuel.md) |  | 
**reactor** | [**ShipReactor**](ShipReactor.md) | [**ShipReactor**](ShipReactor.md) |  | 
**[mounts](#mounts)** | list, tuple,  | tuple,  |  | 
**registration** | [**ShipRegistration**](ShipRegistration.md) | [**ShipRegistration**](ShipRegistration.md) |  | 
**cargo** | [**ShipCargo**](ShipCargo.md) | [**ShipCargo**](ShipCargo.md) |  | 
**[modules](#modules)** | list, tuple,  | tuple,  |  | 
**crew** | [**ShipCrew**](ShipCrew.md) | [**ShipCrew**](ShipCrew.md) |  | 
**frame** | [**ShipFrame**](ShipFrame.md) | [**ShipFrame**](ShipFrame.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# modules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipModule**](ShipModule.md) | [**ShipModule**](ShipModule.md) | [**ShipModule**](ShipModule.md) |  | 

# mounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

