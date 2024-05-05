from flask import Flask, request
from flask import render_template
from pprint import pprint
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

import os

def check_if_log_exists():
    try:
        log_count = pd.read_csv('./static/log_ip.csv', header=0)
        return log_count
    except:
        columns = ['IP','Count']
        log_count = pd.DataFrame(columns=columns)
        log_count.to_csv("./static/log_ip.csv", index=False)
        return log_count

def process_ip_adress():
    """
    Saves the IP address of the person making the request.
    """
    ip_address = request.remote_addr
    df = check_if_log_exists()
    if ip_address in df["IP"].values:
        index_of_ip = np.where(df["IP"].values == ip_address)[0]
        print(index_of_ip)
        df["Count"][index_of_ip] += 1
        df.to_csv("./static/log_ip.csv", index=False)
    else:
        new_row = pd.DataFrame({"IP":[ip_address], "Count":[1]})
        df_append_row = pd.concat([df, new_row], axis=0)
        df_append_row.to_csv("./static/log_ip.csv", index=False)


@app.route("/")
def home():
    process_ip_adress()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
