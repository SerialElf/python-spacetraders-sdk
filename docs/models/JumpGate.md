# openapi_client.model.jump_gate.JumpGate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[connectedSystems](#connectedSystems)** | list, tuple,  | tuple,  | The systems within range of the gate that have a corresponding gate. | 
**jumpRange** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum jump range of the gate. | 
**factionSymbol** | str,  | str,  | The symbol of the faction that owns the gate. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# connectedSystems

The systems within range of the gate that have a corresponding gate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The systems within range of the gate that have a corresponding gate. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectedSystem**](ConnectedSystem.md) | [**ConnectedSystem**](ConnectedSystem.md) | [**ConnectedSystem**](ConnectedSystem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

