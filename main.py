import requests, datetime, json, csv, pandas
from gspreadsheets import get_spreadsheet

def download_exchange_rates(date_to_pull):
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

def download_todays_exchange():
    download_exchange_rates(str(datetime.date.today()))

# def main():
#     # print('main function')


# if __name__ == '__main__':
#     main()

download_todays_exchange()
sheet = get_spreadsheet()
filled_rows_no = len(list(sheet.col_values((1))))
print (filled_rows_no)

try:
    df = pandas.read_csv(str(datetime.date.today())+'.csv')
except IOError:
    print("The searched file was not found")
else:
    print('The shape of the frame is ' + str(df.shape))

col_headers = list(df)
first_col = list(df[col_headers[0]])
input_rows_no = len(first_col)
print(input_rows_no)
print(first_col)
unrolled_list = df.values.tolist()

filled_rows_no+=1
for new_row in unrolled_list:
    print (new_row)