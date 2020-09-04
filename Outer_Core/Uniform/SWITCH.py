print("Non-Uniform Operations Gateway is OPEN. Initiating Process...")
protect_connection('''
conexec.main()
''')
print("Process has ended. Instructions Executed.")
Exterior.SWITCH=False
protect_connection('''sheet.update_cell(2,1,"False")''')
print("Non-Uniform Operations Gateway has been CLOSED.")