from django.shortcuts import render

# from account.models import User
from mpesa.models import xpayMpesa
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

# @login_required()
def transaction(request):
    paymentByUser = xpayMpesa.objects.all()
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/transaction.html', {'payments': paymentByUser}, context)


class TransactionListView(ListView):
    model = xpayMpesa
    template_name = 'dashboard/transaction.html'
    context_object_name = 'transactions'
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        transactions = self.get_queryset()
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


def index(request):
    paymentByUser = xpayMpesa.objects.all()[:5]
    count = xpayMpesa.objects.all().count()
    context = {'count': count}
    return render(request, 'dashboard/index.html', {'payments': paymentByUser}, context)


def active_account(request):
    return render(request, 'dashboard/active_account.html')


def api(request):
    return render(request, 'dashboard/developer/api.html')
