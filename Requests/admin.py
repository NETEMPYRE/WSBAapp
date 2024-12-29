from django.contrib import admin
from .models import Request
import requests

# Register your models here.
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'DateTime', 'RequestID', 'PlayFabID', 'AccountTitle', 'AccountNumber', 'PaymentMethod', 'Amount', 'Status')
    search_fields = ('PlayFabID', 'AccountTitle', 'PaymentMethod')
    list_filter = ('Status', 'PaymentMethod')
        
    def save_model(self, request, obj, form, change):
        if change and 'Status' in form.changed_data and obj.Status == 'Complete':
            title_id = "F5846"
            secret_key = "HZ64KEB18OMNYBNM3P45N98WI5BHUCR6SINKS9TDQ6A4Z8FW37"
            url = f"https://{title_id}.playfabapi.com/Server/ExecuteCloudScript"
            payload = {
                "PlayFabId": obj.PlayFabID,
                "FunctionName": "UpdateWithdrawalRequestStatus",
                "FunctionParameter": {
                    "PlayFabID": obj.PlayFabID,
                    "RequestID": obj.RequestID,
                    "Status": obj.Status,
                },
                "GeneratePlayStreamEvent": True
            }
            headers = {
                "Content-Type": "application/json",
                "X-SecretKey": secret_key
            }
            try:
                response = requests.post(url, json=payload, headers=headers)
                response_data = response.json()
                if response.status_code == 200:
                    self.message_user(request, f"Status Updated Successfully!{response_data}")
                else:
                    self.message_user(
                        request,
                        f"Status Update Failure: {response_data}",
                        level='error'
                    )
            except Exception as e:
                self.message_user(
                    request,
                    f"ERROR! While Calling PlayFab API: {str(e)}",
                    level='error'
                )
        return super().save_model(request, obj, form, change)
    