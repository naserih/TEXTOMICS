import csv

# pain_terms_path = r'C:\Users\FEPC-L389\Google Drive\1_PhDProject\Galenus\data\metamap_pain\pain_terms_i2b2_mimic_.csv'
pain_terms_path = r'C:\Users\FEPC-L389\Google Drive\PhD_McGill\3_SUBMISSIONS\NLP_paper\pain_terms.csv'
pain_terms = ['ache', 'aching', 'angina', 'arthralgia', 'arthrodynia', 'burning', 'cephalalgia', 'cephalgia',
                  'cephalodynia', 'cervicalgia', 'cervicodynia', 'claudication', 'coccyalgia', 'coccydynia',
                  'coccygalgia', 'coccygodynia', 'coccyodynia', 'coccyxdynia', 'coxalgia', ' cp ', 'cramp',
                  'discomfort', 'dolor', 'dorsalgia', 'dorsodynia', 'dysuria', 'esophagodynia', 'glossalgia',
                  'glossalgias', 'glossodynia', 'glossodynias', 'gonalgia', 'inguinodynia', 'lbp', 'lowbacksyndrome',
                  'lumbago', 'lumbagoambiguous', 'lumbalgia', 'meralgia', 'metatarsalgia', 'muscleweakness',
                  'myalgia', 'myalgias', 'myodynia', 'myosalgia', 'neuralgia', 'neuralgias', 'odynophagia',
                  'orchialgia', 'orchidalgia', 'orchidodynia', 'osteodynia', 'otalgia', 'pain', 'pancreatalgia',
                  'postherpeticneuralgia', 'postherpeticneuralgia', 'pressure', 'proctalgia', 'rectalgia',
                  'retrosternal', 'scapulalgia', 'scapulodynia', 'sciatica', 'sore', 'tender', 'tightness', 
                  'mastodynia', 'malaise', 'upset stomach', 'mastalgia'
                 ]
stat = {}
cnt = 0
with open (pain_terms_path, 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        i2b2_pain = row[0]
        mimic_pain = row[1]
        aria_pain = row[2]
        i2b2_error = True
        mimic_error = True
        aria_error = True

        if '(' in i2b2_pain:
            i2b2_pain = i2b2_pain[i2b2_pain.find("(")+1:i2b2_pain.find(")")]
        if '(' in mimic_pain:
            mimic_pain = mimic_pain[mimic_pain.find("(")+1:mimic_pain.find(")")]
        if '(' in aria_pain:
            aria_pain = aria_pain[aria_pain.find("(")+1:aria_pain.find(")")]

        for pain_term in pain_terms:
            if i2b2_pain == "" or pain_term in i2b2_pain:
                i2b2_error = False
            if mimic_pain == "" or pain_term in mimic_pain:
                mimic_error = False
            if aria_pain == "" or pain_term in aria_pain:
                aria_error = False
        if  i2b2_error:
            # print('not_i2b2', i2b2_pain)
            i2b2_pain = ''
        if  mimic_error:
            # print('not_mimic', mimic_pain)
            mimic_pain = ''
        if  aria_error:
            aria_pain = ''
            # print('not_aria', aria_pain)



        cnt += 1
        if i2b2_pain not in stat:
            stat[i2b2_pain] = {'i2b2' : 1}
        else:
            if 'i2b2' not in stat[i2b2_pain]:
                stat[i2b2_pain]['i2b2'] = 1
            else:
                stat[i2b2_pain]['i2b2'] += 1
        if mimic_pain not in stat:
            stat[mimic_pain] = {'mimic' : 1}
        else:
            if 'mimic' not in stat[mimic_pain]:
                stat[mimic_pain]['mimic'] = 1
            else:
                stat[mimic_pain]['mimic'] += 1
        if aria_pain not in stat:
            stat[aria_pain] = {'aria' : 1}
        else:
            if 'aria' not in stat[aria_pain]:
                stat[aria_pain]['aria'] = 1
            else:
                stat[aria_pain]['aria'] += 1

print cnt
with open (pain_terms_path[:-4]+'_out.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['pain term', 'i2b2', 'MIMIC-III', 'ARIA']) 
    for key in stat:
        if 'i2b2' not in stat[key]:
            stat[key]['i2b2'] = 0
        if 'mimic' not in stat[key]:
            stat[key]['mimic'] = 0
        if 'aria' not in stat[key]:
            stat[key]['aria'] = 0
        csvwriter.writerow([key, stat[key]['i2b2'], stat[key]['mimic'],stat[key]['aria']])