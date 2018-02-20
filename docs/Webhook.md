# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_notification_url** | **str** | API url to notify in case of inbound message | [optional] 
**sms_notification_method** | **str** | HTTP method to use for notifying API url in case of inbound message | [optional] 
**sms_notification_fallback_url** | **str** | In case the service for &#x60;sms_notification_url&#x60; is down Karix will hit the fallback url with the incoming message details  | [optional] 
**sms_notification_fallback_method** | **str** | HTTP method to use for fallback notification url | [optional] 
**name** | **str** | Display name of the webhook | [optional] 
**uid** | **str** | Unique ID of the webhook | [optional] 
**created_time** | **datetime** | Date when this webhook was created | [optional] 
**updated_time** | **datetime** | Date when this webhook was last updated | [optional] 
**account_uid** | **str** | UID of Account which created this webhook | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


