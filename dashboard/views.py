from django.shortcuts import render, redirect

# from account.models import User
from django.utils.decorators import method_decorator

from mpesa.models import Transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def transaction(request):
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
    paymentByUser = Transaction.objects.all()[:5]
    count = Transaction.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/index.html', {'transactions': paymentByUser}, context)


@login_required
def active_account(request):
    return render(request, 'dashboard/active_account.html')


@login_required
def api(request):
    if not request.user.is_business:
        return redirect('active')

    return render(request, 'dashboard/developer/api.html')
