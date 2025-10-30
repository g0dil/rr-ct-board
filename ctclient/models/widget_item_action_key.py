from enum import Enum


class WidgetItemActionKey(str, Enum):
    ACTION_APPOINTMENT_DETAILS = "action.appointment.details"
    ACTION_BIRTHDAY_DETAILS = "action.birthday.details"
    ACTION_EVENTFACT_DETAILS = "action.eventfact.details"
    ACTION_EVENT_DETAILS = "action.event.details"
    ACTION_EXCHANGEREQUESTS_ACCEPT = "action.exchangeRequests.accept"
    ACTION_EXCHANGEREQUESTS_CANCEL = "action.exchangeRequests.cancel"
    ACTION_EXCHANGEREQUESTS_DECLINE = "action.exchangeRequests.decline"
    ACTION_EXCHANGEREQUESTS_REQUEST = "action.exchangeRequests.request"
    ACTION_GENERAL_URL = "action.general.url"
    ACTION_GROUP_DETAILS = "action.group.details"
    ACTION_MY_RESOURCES_DETAILS = "action.my-resources.details"
    ACTION_POST_DETAILS = "action.post.details"
    ACTION_SERVICEREQUESTS_ABSENCE = "action.serviceRequests.absence"
    ACTION_SERVICEREQUESTS_ACCEPT = "action.serviceRequests.accept"
    ACTION_SERVICEREQUESTS_COMMENT = "action.serviceRequests.comment"
    ACTION_SERVICEREQUESTS_DECLINE = "action.serviceRequests.decline"
    ACTION_SERVICEREQUESTS_EXCHANGE = "action.serviceRequests.exchange"
    ACTION_SERVICEREQUESTS_UNDO = "action.serviceRequests.undo"
    ACTION_SONGSTOLEARN_DETAILS = "action.songsToLearn.details"

    def __str__(self) -> str:
        return str(self.value)
