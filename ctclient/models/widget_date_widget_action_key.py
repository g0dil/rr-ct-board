from enum import Enum


class WidgetDateWidgetActionKey(str, Enum):
    ACTION_ALLBIRTHDAYS_ALL = "action.allBirthdays.all"
    ACTION_APPOINTMENTS_ALL = "action.appointments.all"
    ACTION_EXCHANGE_REQUESTS_ALL = "action.exchange-requests.all"
    ACTION_FAVORITE_GROUPS_ALL = "action.favorite-groups.all"
    ACTION_GENERAL_URL = "action.general.url"
    ACTION_GROUPMEETING_ALL = "action.groupmeeting.all"
    ACTION_MY_GROUPS_ALL = "action.my-groups.all"
    ACTION_MY_RESOURCES_ALL = "action.my-resources.all"
    ACTION_POSTS_ALL = "action.posts.all"
    ACTION_SERVICE_REQUESTS_ALL = "action.service-requests.all"
    ACTION_SONGSTOLEARN_ALL = "action.songsToLearn.all"
    ACTION_UPCOMING_SERVICES_ALL = "action.upcoming-services.all"

    def __str__(self) -> str:
        return str(self.value)
