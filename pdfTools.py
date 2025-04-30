import PyPDF2

def remove_password(input_pdf, output_pdf):
    # Open the PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if reader.is_encrypted:
            password = input("Enter the password for the PDF: ")
            reader.decrypt(password)

        # Create a writer object to write changes to a new PDF
        writer = PyPDF2.PdfWriter()

        # Copy pages from the input PDF to the writer object
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # Write the new PDF without a password
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

        print("Password removed successfully. New PDF saved as", output_pdf)

def mergePDF(pdf1,pdf2,output):
    writer = PyPDF2.PdfWriter()
    with open(pdf1,'rb') as p1:
        reader = PyPDF2.PdfReader(p1)
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

    with open(pdf2,'rb') as p2:
        reader2 = PyPDF2.PdfReader(p2)
        for page_num in range(len(reader2.pages)):
            writer.add_page(reader.pages[page_num])

    with open(output,'wb') as out_file:
        writer.write(out_file)
    
    print('Both pdfs have been merged to',output)

if __name__ == "__main__":
    print("1)Remove password\n2)Merge PDFs")
    option = int(input('Enter option number'))
    if option==1:
        input_pdf = input("Enter the path to the input PDF file: ").strip('"')
        output_pdf = input("Enter the path to save the output PDF file (without password): ")
        remove_password(input_pdf, output_pdf)
    elif option==2:
        pdf1 = input("Enter the path to first pdf").strip('"')
        pdf2 = input("Enter the path to second pdf").strip('"')
        output_pdf = input("Enter the path to save the output PDF file")
        mergePDF(pdf1,pdf2,output_pdf)

    