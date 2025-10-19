from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MajorUnit
import csv
import io
import openpyxl

def upload_csv(request):
    """Display the CSV/Excel upload page"""
    return render(request, 'upload_csv.html')

def process_csv(request):
    """Process the uploaded CSV or Excel file and save to database"""
    if request.method == 'POST' and request.FILES.get('csv_file'):
        uploaded_file = request.FILES['csv_file']
        file_name = uploaded_file.name.lower()
        
        # Check if file is CSV or Excel
        if not (file_name.endswith('.csv') or file_name.endswith('.xlsx') or file_name.endswith('.xls')):
            messages.error(request, 'Please upload a valid CSV or Excel file (.csv, .xls, .xlsx).')
            return redirect('upload_csv')
        
        try:
            success_count = 0
            error_count = 0
            
            # Process Excel files
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                workbook = openpyxl.load_workbook(uploaded_file)
                sheet = workbook.active
                
                # Get headers from first row
                headers = []
                for cell in sheet[1]:
                    headers.append(cell.value)
                
                # Process each row (skip header row)
                for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                    try:
                        # Create a dictionary from headers and row values
                        row_data = {}
                        for i, header in enumerate(headers):
                            if i < len(row):
                                row_data[header] = str(row[i]) if row[i] is not None else ''
                        
                        MajorUnit.objects.create(
                            image_link=row_data.get('image_link', ''),
                            stock_number=row_data.get('stock_number', ''),
                            mfg=row_data.get('mfg', ''),
                            year=row_data.get('year', ''),
                            model_name=row_data.get('model_name', ''),
                            store=row_data.get('store', ''),
                            quote_level=row_data.get('quote_level', ''),
                            msrp_total=row_data.get('msrp_total', ''),
                            sale_price=row_data.get('sale_price', ''),
                            nap=row_data.get('nap', ''),
                            profit_margin=row_data.get('profit_margin', ''),
                            brochure=row_data.get('brochure', ''),
                            new_edit_modal=row_data.get('new_edit_modal', ''),
                            website_price=row_data.get('website_price', ''),
                            cycle_trader=row_data.get('cycle_trader', ''),
                            location_status=row_data.get('location_status', ''),
                            program=row_data.get('program', ''),
                            days_on_floor=row_data.get('days_on_floor', ''),
                        )
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        print(f"Error processing row {row_num}: {e}")
            
            # Process CSV files
            elif file_name.endswith('.csv'):
                decoded_file = uploaded_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                csv_reader = csv.DictReader(io_string)
                
                for row in csv_reader:
                    try:
                        MajorUnit.objects.create(
                            image_link=row.get('image_link', ''),
                            stock_number=row.get('stock_number', ''),
                            mfg=row.get('mfg', ''),
                            year=row.get('year', ''),
                            model_name=row.get('model_name', ''),
                            store=row.get('store', ''),
                            quote_level=row.get('quote_level', ''),
                            msrp_total=row.get('msrp_total', ''),
                            sale_price=row.get('sale_price', ''),
                            nap=row.get('nap', ''),
                            profit_margin=row.get('profit_margin', ''),
                            brochure=row.get('brochure', ''),
                            new_edit_modal=row.get('new_edit_modal', ''),
                            website_price=row.get('website_price', ''),
                            cycle_trader=row.get('cycle_trader', ''),
                            location_status=row.get('location_status', ''),
                            program=row.get('program', ''),
                            days_on_floor=row.get('days_on_floor', ''),
                        )
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        print(f"Error processing row: {e}")
            
            # Success message
            if success_count > 0:
                messages.success(request, f'Successfully imported {success_count} records!')
            if error_count > 0:
                messages.warning(request, f'{error_count} records failed to import.')
                
        except Exception as e:
            messages.error(request, f'Error processing file: {str(e)}')
            return redirect('upload_csv')
    
    else:
        messages.error(request, 'No file was uploaded.')
    
    return redirect('upload_csv')

def view_units(request):
    """View all major units"""
    units = MajorUnit.objects.all()
    return render(request, 'view_units.html', {'units': units})

# New views for all pages
def landing_page(request):
    """Display landing page"""
    return render(request, 'landingpage.html')

def login_page(request):
    """Display login page"""
    return render(request, 'login.html')

def dashboard(request):
    """Display dashboard"""
    return render(request, 'dashboard.html')

def commission(request):
    """Display commission page"""
    return render(request, 'commission.html')

def contact(request):
    """Display contact page"""
    return render(request, 'contact.html')

def coupons(request):
    """Display coupons page"""
    return render(request, 'coupons.html')

def cycle_trade_units(request):
    """Display cycle trade units page"""
    return render(request, 'cycletradeunits.html')

def major_units_grid(request):
    """Display major units grid page"""
    return render(request, 'majorunitsgrid.html')

def mu_missing(request):
    """Display MU missing page"""
    return render(request, 'mumissing.html')

def quotes(request):
    """Display quotes page"""
    return render(request, 'quotes.html')

def quote_view(request):
    """Display quote view page"""
    return render(request, 'quote.html')

def portal_quote(request):
    """Display portal quote page"""
    return render(request, 'portalquote.html')

def sale_program_edit(request, program_id):
    """Edit sale program by ID"""
    # You can later use program_id to fetch a record from the database.
    context = {'program_id': program_id}
    return render(request, 'saleprogramedit.html', context)

def sale_programs(request):
    """Display sale programs page"""
    return render(request, 'saleprograms.html')