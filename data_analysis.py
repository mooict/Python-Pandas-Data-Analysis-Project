# This script is created by MOO ICT
# It is designed for educational purpose only

#Versions
#matplotlib                3.7.1
#pandas                    1.5.3
#Python                    3.8.0

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
programming_running = True

product_names = df["Produce"].values.tolist()
dates = df.columns.tolist()
dates.remove("Produce")

# Unicode Emoji's
wrong_symbol = '\u26D4'
right_symbol = '\u2705'
search_symbol = "\U0001F50D"
chart_symbol = "\U0001F4CA"
good_bye = "\U0001F44B"




def display_options():
    print("Choose an option from below: ")
    print("[1] -- See the whole data set")
    print("[2] -- Sort Item Names in Ascending order")
    print("[3] -- Sort Item Names in Descending order")
    print("[4] -- Show All Available Products")
    print("[5] -- Show All Available Dates")
    print("[6] -- " + search_symbol + " Search Date Range for all items")
    print("[7] -- " + search_symbol + " Search Item Name, Start Date and End Date")
    print("[8] -- " + chart_symbol + " Show Total Sales Per Item In a Chart")
    print("[9] -- " + chart_symbol + " Show Average Sales Per Item In a Chart")
    print("[10] -- " + chart_symbol + " Show Chart for Entire Data Set")
    print("[11] -- " + wrong_symbol + " Exit the Program")


def show_full_dataset():
    print(df.to_string())

def sort_dataset(switch):
    sortedDF = df.sort_values("Produce", ascending=switch)
    sortedDF = sortedDF.reset_index(drop=True)
    print(sortedDF.to_string())

def show_average():
    df2 = df.copy()
    df2["Average Sales"] = df2.iloc[:, 1:].mean(axis=1)
    df2["Average Sales"] = df2["Average Sales"].round().astype("int")
    df2 = df2[["Produce", "Average Sales"]]
    print(df2.to_string())
    make_charts(df2)

def show_total():
    df2 = df.copy()
    df2["Total Sales"] = df2.iloc[:, 1:].sum(axis=1)
    df2 = df2[["Produce", "Total Sales"]]
    print(df2.to_string())
    make_charts(df2)

def product_name_dates(name, start, end):
    df2 = df.loc[:, start:end]
    df2.insert(0, "Produce", value=df.loc[:, "Produce"])
    df2["Total Sales"] = df2.iloc[:, 1:].sum(axis=1)
    if name == "":
        print(df2)
        make_charts_with_transpose(df2)
    else: 
        df3 = df2.loc[(df["Produce"] == name)]
        print(df3)
        make_charts_with_transpose(df3)

def make_charts_with_transpose(dataframe):
    chartDF = dataframe.copy()
    chartDF.set_index("Produce", inplace=True)
    chartDF = chartDF.T # transpose
    chartDF.plot(kind="bar")
    plt.xticks(rotation = 30)
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)
    plt.show()

def make_charts(dataframe):
    chartDF = dataframe.copy()
    chartDF = chartDF.set_index("Produce")
    chartDF.plot(kind="bar")
    plt.xticks(rotation = 30)
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)
    plt.show()

def capture_user_input(on_item, from_start, to_end):
    
    while on_item or from_start or to_end:
        item_name = ""

        if on_item:
            item_name = input(search_symbol + " Enter the Item Name:           ")
            item_name = item_name.title()
            if item_name in product_names:
                print(right_symbol +  " Item " + item_name + " is found")
                on_item = False
                from_start = True
            else:
                print(wrong_symbol + " " + item_name + " is not found, try again")
                from_start = False
                to_end = False
        if from_start: 
            start_date = input(search_symbol + " Enter the start date: DD/MM/YYYY       ")

            if start_date in dates:
                print(right_symbol +  " " + start_date + " is valid")
                start_index = dates.index(start_date)
                from_start = False
                to_end = True
            else: 
                print(wrong_symbol + " " + start_date + " is not valid, try again")
                from_start = True
                to_end = False
        if to_end:
            end_date = input(search_symbol + " Enter the end date: DD/MM/YYYY           ")
            if end_date in dates: 
                print(right_symbol +  " " + end_date + " is valid")
                end_index = dates.index(end_date)
                if start_index >= end_index:
                    print("End date cannot be the same or before the start date")
                    print("Enter Start and End Date Again")
                    from_start = True
                    to_end = False
                else:
                    to_end = False
                    product_name_dates(item_name, start_date, end_date)
            else:
                print(wrong_symbol + " " + end_date + " is not valid, try again")


while programming_running: 
    display_options()
    user_input = input("Enter a selection......")
    # if statements below for the user input
    if user_input == "1":
        print("The Full Data Set is displayed below: ")
        show_full_dataset()
    elif user_input == "2":
        print("Product name is asending order")
        sort_dataset(True)
    elif user_input == "3":
        print("Produce names in descending order")
        sort_dataset(False)
    elif user_input == "4":
        print("All available products: ")
        print(product_names)
    elif user_input == "5":
        print("All available dates are: ")
        print(dates)
    elif user_input == "6":
        print("Enter Range of Dates to search")
        capture_user_input(False, True, True)
    elif user_input == "7":
        print("Enter Item Name, Start Date and End Date to search")
        capture_user_input(True, True, True)
    elif user_input == "8":
        print("Showing the Total Sales per Item")
        show_total()
    elif user_input == "9":
        print("Showing Average Sales per Items")
        show_average()
    elif user_input == "10":
        print("Showing the chart for the data set")
        make_charts_with_transpose(df)
    elif user_input == "11":
        print(good_bye + " Good Bye and Have a Good Day")
        break
