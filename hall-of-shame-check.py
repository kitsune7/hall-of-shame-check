import urllib.request

offenders_url = 'https://raw.githubusercontent.com/plaintextoffenders/plaintextoffenders/master/offenders.csv'
with urllib.request.urlopen(offenders_url) as response:
    csv_text = response.read()

offender_list = csv_text.decode('utf-8').split('\n')[1:]
offender_map = {}
for i in range(len(offender_list)):
    item = offender_list[i].split(',')
    if len(item) > 1:
        offender_map[item[0]] = item[1]

check_input = input('Domain name of site: ')
if check_input in offender_map:
    print(check_input + ' is a recognized offender. (' + offender_map[check_input] + ')')
else:
    print('This site is not a known offender.')

