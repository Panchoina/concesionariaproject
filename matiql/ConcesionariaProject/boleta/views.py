from io import BytesIO
from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from .models import boleta

#Funciones para la boleta

# crear boleta
def GenerarBoleta(request):
    return render(request,"")


# imprimir boleta a pdf
def ImprimirBoleta(request, folio):
    # Obtener la boleta específica de la base de datos
    boleta_obj = boleta.objects.get(folio=folio)
    
    # Datos que queremos incluir en el PDF (puedes personalizarlos como desees)
    data = [
        ['Folio', str(boleta_obj.folio)],
        ['Monto', str(boleta_obj.monto)],
        ['Dirección', boleta_obj.direccion],
        ['Fecha', boleta_obj.fecha.strftime('%Y-%m-%d %H:%M:%S')],
        ['Fono Empleado', str(boleta_obj.FonoEmpleado.FonoEmpleado)],  # Suponiendo que la relación es correcta
        ['Fono Cliente', str(boleta_obj.FonoCliente.FonoCliente)],    # Suponiendo que la relación es correcta
        ['Vendedor', boleta_obj.vendedor.nombre],  # Aquí ajustas para que obtenga el nombre o lo que necesites del vendedor
    ]

    # Crear un documento PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Crear los estilos para el PDF
    styles = getSampleStyleSheet()
    elementos = []

    # Título del documento (opcional)
    titulo = Paragraph("Boleta de Venta", styles['Title'])
    elementos.append(titulo)

    # Crear la tabla con los datos de la boleta
    tabla = Table(data)
    
    # Estilo de la tabla
    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ])
    tabla.setStyle(estilo)
    
    # Agregar la tabla al documento
    elementos.append(tabla)

    # Generar el PDF
    doc.build(elementos)
    
    # Mover el puntero de buffer al inicio del archivo PDF
    buffer.seek(0)
    
    # Devolver el PDF como respuesta para la descarga
    return FileResponse(buffer, as_attachment=True, filename=f"boleta_{folio}.pdf")