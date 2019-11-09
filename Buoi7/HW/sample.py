with open('input.csv') as f:
    f.readline()                    # Header row
    rows = f.readlines()

sales = {}

for row in rows:
    product, qty, price, cost = row.strip().split(',')
    if product not in sales:
        sales[product] = {'qty':0,'sale': 0, 'profit': 0}

    qty = int(qty)
    price = int(price)
    cost = int(cost)
    sales[product]['qty'] += qty                   
    sales[product]['sale'] += qty*price
    sales[product]['profit'] += qty*(price-cost)

sale_items = sorted(sales.items(), key=lambda x:x[1]['sale'], reverse=True)
with open('sales_output.csv','w') as f:
    f.write('MaSP,SoLuong,DoanhSo,LoiNhuan\n')
    for product, sale in sale_items:
        f.write(f'{product},{sale["qty"]},{sale["sale"]},{sale["profit"]}\n')
    
