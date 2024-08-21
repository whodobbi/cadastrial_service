from django.urls import path

from query.views import QueryView, ResultView, PingView, HistoryView

urlpatterns = [
    path("query/", QueryView.as_view(), name="query"),
    path("result/", ResultView.as_view(), name="result"),
    path("ping/", PingView.as_view(), name="ping"),
    path("history/", HistoryView.as_view(), name="history"),
]
