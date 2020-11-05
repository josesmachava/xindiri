import datetime

from django.shortcuts import render, redirect

# from account.models import User
from django.utils.decorators import method_decorator

from mpesa.models import Transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def transaction(request):
    if not request.user.is_business:
        return redirect('active')
    paymentByUser = Transaction.objects.all()
    count = Transaction.objects.all().count()
    context = {'count': count}
    return render(request, '3dashboard/transaction.html', {'payments': paymentByUser}, context)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'dashboard/transaction.html'
    context_object_name = 'transactions'
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        transactions = Transaction.objects.all().filter(api_key="23b694b0fa9cdb8270ea1045d5ef9f68")
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
    if request.user.is_business:
        return redirect('active')
    transaction = Transaction.objects.all()[:10]
    total_amount = Transaction.objects.filter(transaction_status_code="201").aggregate(Sum('amount'))
    today = datetime.date.today()
    week = today - datetime.timedelta(days=7)
    month = today - datetime.timedelta(days=31)
    format_day = today.strftime("%Y-%m-%d")
    today_amount = Transaction.objects.filter(transaction_status_code="201", created_at=today).aggregate(Sum('amount'))
    week_amount = Transaction.objects.filter(transaction_status_code="201", created_at__range=[week, today]).aggregate(Sum('amount'))
    month_amount = Transaction.objects.filter(transaction_status_code="201", created_at__range=[month, today]).aggregate(
        Sum('amount'))

    return render(request, 'dashboard/index.html', {'transactions': transaction,
                                                    'total_amount': total_amount['amount__sum'],
                                                    "today_amount": today_amount['amount__sum'],
                                                    "week_amount": week_amount['amount__sum'],
                                                    "month_amount": month_amount['amount__sum']
                                                    })

@login_required
def active_account(request):
    return render(request, 'dashboard/active_account.html')


@login_required
def api(request):
    if  request.user.is_business:
        return redirect('active')

    return render(request, 'dashboard/developer/api.html')
