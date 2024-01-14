from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(bill, bill_products):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cek_{bill.id}.pdf"'

    # Create the PDF object
    p = canvas.Canvas(response, pagesize=letter)

    # Add content to the PDF
    p.drawString(380, 720, f"Cek id: {bill.id}")
    p.drawString(380, 700, f"Umumy bahasy: {bill.total_price} TMT")
    p.drawString(380, 680, f"Senesi: {bill.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    # Add table header
    data = [['Harydyn ady', 'Mukdary', 'Umumy (TMT)']]

    # Add data from related BillProducts
    for bill_product in bill_products:
        unit = 'stuk' if bill_product.product.unit == 'piece' else 'kg'
        data.append([bill_product.product.name, f'{bill_product.count} {unit}', str(bill_product.total_price)])

    # Create the table
    table = Table(data)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)

    # Draw the table on the PDF
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 80, 660)

    # Close the PDF object
    p.showPage()
    p.save()

    return response