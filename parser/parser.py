import csv
print 'CSV Parser'


procedure_file = open('procedures.txt', 'w')
patient_file = open('patients.txt', 'w')

with open('RiversMaster.csv','r' ) as csvfile:
    patient_list_duplicates=list()
    procedure_list_duplicates=list()
    data=csv.reader(csvfile, quotechar='|')
    for row in data:
        patient_name=row[0]
        procedure_name=row[1]
        patient_list_duplicates.append(patient_name)
        procedure_list_duplicates.append(procedure_name)


#    print patient_list
    patient_list_duplicates.pop()
    procedure_list_duplicates.pop()
    print 'Total Names in File'
    print len(patient_list_duplicates)
    print 'Total Procedures in File'
    print len(procedure_list_duplicates)

    patient_list=set(patient_list_duplicates)
    print 'Unique Names in File'
    print len(patient_list)

    procedure_list=set(procedure_list_duplicates)
    print 'Unique Procedures in File'
    print len(procedure_list)
    print '======================='
    print procedure_list
    print patient_list
    for row in patient_list:
        patient_file.write(row + '\n')
    for row in procedure_list:
        procedure_file.write(row + '\n')

patient_file.close()
procedure_file.close()
csvfile.close()
