import requests, datetime, json, csv, pandas
from gspreadsheets import get_spreadsheet

def download_exchange_rates_to_csv(date_to_pull):
    """This will download the exchange rates info from website https://exchangeratesapi.io/
    for the specifed date"""

    url = "https://api.exchangeratesapi.io/"
    r = requests.get(url + date_to_pull)
    j = json.loads(r.text)

    with open(date_to_pull + ".csv", 'wb') as f:
        c = csv.writer(f)
        c.writerow(['Currencty', 'Exchange rate(EUR)', 'Date'])
        for curr in j['rates']:
            c.writerow([curr, j['rates'][curr], date_to_pull])

def download_todays_exchange_to_csv():
    download_exchange_rates_to_csv(str(datetime.date.today()))

# def main():
#     # print('main function')


# if __name__ == '__main__':
#     main()

# download_todays_exchange_to_csv()
sheet = get_spreadsheet()
filled_rows_no = len(list(sheet.col_values((1))))

try:
    df = pandas.read_csv(str(datetime.date.today())+'.csv')
except IOError:
    print("The searched file was not found")
else:
    print('The shape of the frame is ' + str(df.shape))
unrolled_list = df.values.tolist()

sh = sheet.spreadsheet

sh.values_update(
    'Arkusz1!A%d' % (filled_rows_no+1),
    params={'valueInputOption': 'RAW'},
    body={'values': unrolled_list}
)