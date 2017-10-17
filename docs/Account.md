# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the account. Must be unique within the parent account.  | 
**status** | **str** | Status of your account. Possible values are:   - enabled: Account is ready to be used   - suspended: Account has been temporarily suspended   - disabled: Account has been permanently disabled and             cannot be revived. All resources allocated             to the subaccount like phonenumbers are also             deleted.  | [optional] 
**uid** | **str** | Alphanumeric user identification. Used as username for Basic Authentication  | [optional] 
**token** | **str** | Token password for this account. Used as password in Basic Authentication  | [optional] 
**is_parent** | **bool** | There is generally only one parent account in list. Rest are child subaccounts. Possible values:   - &#x60;true&#x60;: If the account is a parent account   - &#x60;false&#x60;: If the account is a subaccount with a parent account  | [optional] 
**created_time** | **datetime** | Date when this account was created | [optional] 
**updated_time** | **datetime** | Date when this account was last updated | [optional] 
**account_type** | **str** | Signifies whether the account is prepaid or postpaid  | [optional] 
**credit_balance** | **float** | Account&#39;s credit balance in US dollars. For subaccounts this value will be &#x60;null&#x60;.  | [optional] 
**auto_recharge** | **bool** | Whether auto-recharge has been enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


