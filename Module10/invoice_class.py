class Invoice:
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price={}):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.address = address
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.items_with_price = items_with_price

    def __str__(self):
        return f"Invoice {self.invoice_id} for {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Invoice({self.invoice_id}, {self.customer_id}, {self.address}, {self.last_name}, {self.first_name}, {self.phone_number}, {self.items_with_price})"

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        total = sum(self.items_with_price.values())
        tax = round(total * 0.06, 2)
        grand_total = total + tax
        for item, price in self.items_with_price.items():
            print(f"{item}.....${price:.2f}")
        print(f"Tax......... ${tax:.2f}")
        print(f"Total.......${grand_total:.2f}")

if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
