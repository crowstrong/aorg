from django.urls import path

from subscription.views import (CancelSubscriptionView, SubscribeView,
                                SubscriptionDetailView, SubscriptionListView,
                                UpdateSubscriptionView)

app_name = "subscription"

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("subscriptions/", SubscriptionListView.as_view(), name="subscriptions_list"),
    path("subscriptions/<int:subscription_id>/", SubscriptionDetailView.as_view(), name="subscription_detail"),
    path("subscriptions/<int:subscription_id>/update/", UpdateSubscriptionView.as_view(), name="update_subscription"),
    path("subscriptions/<int:subscription_id>/cancel/", CancelSubscriptionView.as_view(), name="cancel_subscription"),
]
