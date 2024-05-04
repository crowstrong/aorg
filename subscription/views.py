from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from subscription.forms import SubscriptionForm
from subscription.models import Subscription


class SubscribeView(View):
    def get(self, request):
        form = SubscriptionForm()
        return render(request, "subscribe.html", {"form": form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            messages.success(request, "Подписка успешно оформлена.")
            return redirect("subscriptions_list")
        return render(request, "subscribe.html", {"form": form})


class SubscriptionListView(View):
    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, "subscriptions_list.html", {"subscriptions": subscriptions})


class SubscriptionDetailView(View):
    def get(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        return render(request, "subscription_detail.html", {"subscription": subscription})


class UpdateSubscriptionView(View):
    def get(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        form = SubscriptionForm(instance=subscription)
        return render(request, "update_subscription.html", {"form": form})

    def post(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, "Подписка успешно обновлена.")
            return redirect("subscription_detail", subscription_id=subscription_id)
        return render(request, "update_subscription.html", {"form": form})


class CancelSubscriptionView(View):
    def post(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        subscription.delete()
        messages.success(request, "Подписка успешно отменена.")
        return redirect("subscriptions_list")
