# CreateAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the account. Must be unique within the parent account.  | 
**status** | **str** | Status of your account. Possible values are:   - enabled: Account is ready to be used   - suspended: Account has been temporarily suspended   - disabled: Account has been permanently disabled and             cannot be revived. All resources allocated             to the subaccount like phonenumbers are also             deleted.   &#x60;suspended&#x60; and &#x60;disabled&#x60; accounts cannot use Karix API. They will receive   &#x60;403 Forbidden&#x60; response.  | [optional] [default to 'enabled']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


