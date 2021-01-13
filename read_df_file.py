import pandas
import requests
import json

def read_sheet():
    googleSheetId = '1TzDXLdhjrUjHo4Jj5CY5RNd-mxh1kjksuXVeQqhk3i0'
    worksheetName = 'Demo'
    URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    	googleSheetId,
    	worksheetName
    )
    df = pandas.read_csv(URL, index_col=False)
    return df

def save_in_db_new_entry():
    df = read_sheet()
    with open("file.json") as file:
        data = json.load(file)
    if len(df) > len(data["new_entry"]):
        get_lenth = len(df) - len(data["new_entry"])
        last_row_df = df.tail(get_lenth)
        for i in range(len(last_row_df)):
          timestamp = last_row_df.iloc[i, 0]
          email = last_row_df.iloc[i, 1]
          name = last_row_df.iloc[i, 2]
          city = last_row_df.iloc[i, 3]
          contact = last_row_df.iloc[i, 4]
          age = last_row_df.iloc[i, 5]
          recent_company = last_row_df.iloc[i, 6]
          role_in_company = last_row_df.iloc[i, 7]
          current_ctc = last_row_df.iloc[i, 8]
          fixed_component_ctc = last_row_df.iloc[i, 9]
          experience = last_row_df.iloc[i, 10]
          comfort = last_row_df.iloc[i, 11]
          relocate = last_row_df.iloc[i, 12]
          rate_english = last_row_df.iloc[i, 13]
          skills = last_row_df.iloc[i, 14]
          industries = last_row_df.iloc[i, 15]
          profile = last_row_df.iloc[i, 16]
          factors = last_row_df.iloc[i, 17]
          dict_to_insert = {
              "timestamp": timestamp,
              "email": email,
              "name": name,
              "city": city,
              "contact": contact,
              "age": age,
              "recent_company": recent_company,
              "role_in_company": role_in_company,
              "current_ctc": current_ctc,
              "Fixed_component_ctc": fixed_component_ctc,
              "experience": experience,
              "comfort": comfort,
              "relocate": relocate,
              "rate_english": rate_english,
              "skills": skills,
              "industries": industries,
              "profile": profile,
              "factors": factors
          }
          posting_api = requests.post("http://127.0.0.1:8000/items/insert/", json=dict_to_insert)
          print("Data Posted Via API")
    elif len(df) == len(data["new_entry"]):
        return "No new Entry"

if __name__ == "__main__":
    save_in_db_new_entry()