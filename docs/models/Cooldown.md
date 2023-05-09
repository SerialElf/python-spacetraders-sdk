# openapi_client.model.cooldown.Cooldown

A cooldown is a period of time in which a ship cannot perform certain actions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A cooldown is a period of time in which a ship cannot perform certain actions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**remainingSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | The remaining duration of the cooldown in seconds | 
**totalSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | The total duration of the cooldown in seconds | 
**expiration** | str, datetime,  | str,  | The date and time when the cooldown expires in ISO 8601 format | value must conform to RFC-3339 date-time
**shipSymbol** | str,  | str,  | The symbol of the ship that is on cooldown | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

