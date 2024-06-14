from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

def index(request):
    accounts = Account.objects.all()
    return render(request, 'finance/index.html', {'accounts': accounts})

def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account added successfully.')
            return redirect('index')
    else:
        form = AccountForm()
    return render(request, 'finance/add_account.html', {'form': form})

def add_transaction(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            if transaction.type == 'deposit':
                account.balance += transaction.amount
            elif transaction.type == 'withdrawal':
                account.balance -= transaction.amount
            account.save()
            transaction.save()
            messages.success(request, 'Transaction added successfully.')
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'finance/add_transaction.html', {'form': form, 'account': account})

def view_transactions(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'finance/view_transactions.html', {'account': account, 'transactions': transactions})


def delete_account(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        account.delete()
        messages.success(request, 'Account deleted successfully.')
        return redirect('index')
    return render(request, 'finance/delete_account.html', {'account': account})