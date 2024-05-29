# David Metcalfe, James Masters, Antonella Delmestri, Andrew Judge, Daniel Perry, Cheryl Zogg, Belinda Gabbe, Matthew Costa, 2024.

import sys, csv, re

codes = [{"code":"K100000","system":"readv2"},{"code":"K0A3000","system":"readv2"},{"code":"K100.00","system":"readv2"},{"code":"K100100","system":"readv2"},{"code":"K0A0100","system":"readv2"},{"code":"K100600","system":"readv2"},{"code":"K100500","system":"readv2"},{"code":"K0A0000","system":"readv2"},{"code":"K101000","system":"readv2"},{"code":"K101100","system":"readv2"},{"code":"K100z00","system":"readv2"},{"code":"K104.00","system":"readv2"},{"code":"K0A0600","system":"readv2"},{"code":"K03V.00","system":"readv2"},{"code":"K0A3600","system":"readv2"},{"code":"K10y300","system":"readv2"},{"code":"K100400","system":"readv2"},{"code":"K0A3.00","system":"readv2"},{"code":"K0A0.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-elixhauser-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-elixhauser-primary-care-nephrit---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-elixhauser-primary-care-nephrit---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-elixhauser-primary-care-nephrit---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
