# David Metcalfe, James Masters, Antonella Delmestri, Andrew Judge, Daniel Perry, Cheryl Zogg, Belinda Gabbe, Matthew Costa, 2024.

import sys, csv, re

codes = [{"code":"8882.00","system":"readv2"},{"code":"7L1B000","system":"readv2"},{"code":"7L1A100","system":"readv2"},{"code":"ZV45100","system":"readv2"},{"code":"TB11.11","system":"readv2"},{"code":"Gy10.00","system":"readv2"},{"code":"ZV56.00","system":"readv2"},{"code":"SP07G00","system":"readv2"},{"code":"7257300","system":"readv2"},{"code":"G72C.00","system":"readv2"},{"code":"TA02000","system":"readv2"},{"code":"F447C00","system":"readv2"},{"code":"ZV56y11","system":"readv2"},{"code":"7L1A011","system":"readv2"},{"code":"Gy60.00","system":"readv2"},{"code":"Gy31.00","system":"readv2"},{"code":"SP01500","system":"readv2"},{"code":"7L1B.11","system":"readv2"},{"code":"ZV56100","system":"readv2"},{"code":"Gy21.00","system":"readv2"},{"code":"SP0E.00","system":"readv2"},{"code":"14V2.00","system":"readv2"},{"code":"Z1A1.00","system":"readv2"},{"code":"G72D200","system":"readv2"},{"code":"7L1A.11","system":"readv2"},{"code":"G72D100","system":"readv2"},{"code":"4I29.00","system":"readv2"},{"code":"7L1A400","system":"readv2"},{"code":"Gy40.00","system":"readv2"},{"code":"TA22000","system":"readv2"},{"code":"SP05613","system":"readv2"},{"code":"G72D.00","system":"readv2"},{"code":"Gy3..00","system":"readv2"},{"code":"7L1A000","system":"readv2"},{"code":"Z1A..00","system":"readv2"},{"code":"7A60600","system":"readv2"},{"code":"ZV56011","system":"readv2"},{"code":"7L1A600","system":"readv2"},{"code":"14V2.11","system":"readv2"},{"code":"ZV56z00","system":"readv2"},{"code":"7L1B200","system":"readv2"},{"code":"Gy1..00","system":"readv2"},{"code":"ZVu3G00","system":"readv2"},{"code":"ZV56y00","system":"readv2"},{"code":"Gy41.00","system":"readv2"},{"code":"TB11.00","system":"readv2"},{"code":"7L1B100","system":"readv2"},{"code":"Z91A.00","system":"readv2"},{"code":"Gy30.00","system":"readv2"},{"code":"7L1C000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-elixhauser-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-elixhauser-primary-care-iridodialysis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-elixhauser-primary-care-iridodialysis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-elixhauser-primary-care-iridodialysis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
