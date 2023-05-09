# openapi_client.model.ship_requirements.ShipRequirements

The requirements for installation on a ship

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The requirements for installation on a ship | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**power** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of power required from the reactor. | [optional] 
**crew** | decimal.Decimal, int,  | decimal.Decimal,  | The number of crew required for operation. | [optional] 
**slots** | decimal.Decimal, int,  | decimal.Decimal,  | The number of module slots required for installation. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

