# David Metcalfe, James Masters, Antonella Delmestri, Andrew Judge, Daniel Perry, Cheryl Zogg, Belinda Gabbe, Matthew Costa, 2024.

import sys, csv, re

codes = [{"code":"SP08F00","system":"readv2"},{"code":"TB00111","system":"readv2"},{"code":"SP08G00","system":"readv2"},{"code":"SP08D00","system":"readv2"},{"code":"SP08R00","system":"readv2"},{"code":"7B06300","system":"readv2"},{"code":"SP08E00","system":"readv2"},{"code":"SP08W00","system":"readv2"},{"code":"SP08H00","system":"readv2"},{"code":"TB00100","system":"readv2"},{"code":"SP08T00","system":"readv2"},{"code":"7B00500","system":"readv2"},{"code":"SP08V00","system":"readv2"},{"code":"67P4100","system":"readv2"},{"code":"7B00200","system":"readv2"},{"code":"7B00212","system":"readv2"},{"code":"661M200","system":"readv2"},{"code":"SP08N00","system":"readv2"},{"code":"7B00211","system":"readv2"},{"code":"SP08300","system":"readv2"},{"code":"7B00600","system":"readv2"},{"code":"SP08J00","system":"readv2"},{"code":"8L50.00","system":"readv2"},{"code":"7B0Fz00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-elixhauser-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-elixhauser-primary-care-transplantation---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-elixhauser-primary-care-transplantation---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-elixhauser-primary-care-transplantation---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
