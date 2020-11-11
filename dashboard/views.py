import datetime

from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

# from account.models import User
from django.utils.decorators import method_decorator

from account.models import Api
from mpesa.models import Transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'dashboard/transaction.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        print(self.request.user)
        transactions  = Transaction.objects.filter(user=self.request.user)
        print(transactions)
        page = self.request.GET.get('page')
        paginator = Paginator(transactions, self.paginate_by)
        try:
            transactions = paginator.page(page)
        except PageNotAnInteger:
            transactions = paginator.page(1)
        except EmptyPage:
            transactions = paginator.page(paginator.num_pages)
        context['transaction'] = transactions
        return context


@login_required
def index(request):
    if not request.user.is_business:
        return redirect('active')

    transaction = Transaction.objects.filter(user=request.user)[:10]
    total_amount = Transaction.objects.filter(transaction_status_code="201", is_active=True, user=request.user).aggregate(total_amount=Coalesce(Sum('amount'), 0))
    today = datetime.date.today()
    week = today - datetime.timedelta(days=7)
    month = today - datetime.timedelta(days=31)
    format_day = today.strftime("%Y-%m-%d")
    today_amount = Transaction.objects.filter(transaction_status_code="201", is_active=True, user=request.user, created_at=today).aggregate(today_amount=Coalesce(Sum('amount'), 0))
    week_amount = Transaction.objects.filter(transaction_status_code="201", is_active=True, user=request.user, created_at__range=[week, today]).aggregate(week_amount=Coalesce(Sum('amount'), 0))
    month_amount = Transaction.objects.filter(transaction_status_code="201", is_active=True, user=request.user,  created_at__range=[month, today]).aggregate(month_amount=Coalesce(Sum('amount'),0))

    return render(request, 'dashboard/index.html', {'transactions': transaction,
                                                    'total_amount': total_amount['total_amount'],
                                                    "today_amount": today_amount['today_amount'],
                                                    "week_amount": week_amount['week_amount'],
                                                    "month_amount": month_amount['month_amount']
                                                    })

@login_required
def active_account(request):
    return render(request, 'dashboard/active_account.html')


@login_required
def api(request):
    api = Api.objects.get(user=request.user)

    return render(request, 'dashboard/developer/api.html', {"api":api, "all":all})
