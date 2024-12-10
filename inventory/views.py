from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item
from .forms import ItemForm


def shop(request):
    items = Item.objects.all()

    if request.method == "POST":
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        
        # Fetch the item being bought
        item = Item.objects.get(id=item_id)
        
        # Check if the requested quantity is available
        if item.quantity_in_stock >= quantity:
            item.quantity_in_stock -= quantity  # Deduct the quantity
            item.save()  # Save the updated item
            messages.success(request, f"Successfully bought {quantity} of {item.name}")
        else:
            messages.error(request, "Insufficient stock available")

        return redirect('shop')  # Redirect to shop page after purchase

    return render(request, 'inventory/shop.html', {'items': items})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})

def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists in your templates folder


def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_edit.html', {'form': form})

def item_add(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/item_edit.html', {'form': form})

