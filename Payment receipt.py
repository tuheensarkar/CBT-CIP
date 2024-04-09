from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_receipt(customer_name, payment_method, items):
    current_datetime = datetime.now().strftime("%Y-%m-%d ")

    c = canvas.Canvas(filename="receipt.pdf", pagesize=A4)

    c.setFillColorRGB(0.9,0.9,0.9)
    c.rect(0,0,A4[0],A4[1],fill=1)
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    heading_style = styles["Heading1"]

    c.setFont("Helvetica-Bold", 20)
    c.setFillColorRGB(0,0,0)
    c.drawCentredString(300, 750, "Invoice")
    c.drawCentredString(300, 730, "-" * 80)

    c.setFont("Helvetica", 12)
    c.drawString(50, 700, "Customer Name:")
    c.drawString(200, 700, customer_name)
    c.drawString(50, 680, "Date:")
    c.drawString(200, 680, current_datetime)

    c.drawString(50, 650, "Payment Method:")
    c.drawString(200, 650, payment_method)
    c.setStrokeColorRGB(1, 0, 0)
    c.line(50,645 , 400,645 )
    c.drawString(50,620,"Items")
    c.drawString(200, 620, "Qty")
    c.drawString(350, 620, "Price")
    y_position = 560
    total=0
    for item, details in items.items():
        quantity,price = details
        total=total+(price*quantity)
        c.drawString(50, y_position, f"{item} ")
        c.drawString(200, y_position, f"{quantity} ")
        c.drawString(350,y_position,f"Rs{price * quantity}")
        y_position -= 20

    c.line(50,y_position,400,y_position)
    c.setStrokeColorRGB(1, 0, 0)
    c.drawString(50, y_position - 20, f"Total:")
    c.drawString(350,y_position-20,f"Rs{total}")

    c.setFont("Helvetica", 10)
    c.drawString(50, 50, "Thank you for your business!")

    print("Your Invoice is generated")
    c.save()


def get_items_from_user():
    items = {}
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == "done":
            break
        item_quantity= int(input("Enter item quantity: "))
        item_price = float(input("Enter item price: "))
        items[item_name] = (item_quantity,item_price)
    return items


customer_name = input("Enter your name: ")
payment_method = input("Enter your payment Method: ")
items = get_items_from_user()

generate_receipt(customer_name, payment_method, items)