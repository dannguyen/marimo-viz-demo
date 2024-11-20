import marimo

__generated_with = "0.9.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(mo, xvar_picker, yvar_picker):
    mo.md(f"""# Silly State Census Plot Demo
    Source: [Google BigQuery Public Dataset: bigquery-public-data.census_bureau_acs.state_2020_5yr](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2scensus_bureau_acs!3sstate_2020_5yr)


    Choose **x variable**: {xvar_picker}

    Choose **y variable**: {yvar_picker}
    """)
    return


@app.cell(hide_code=True)
def __(df, plt, xvar, yvar):
    plt.figure(figsize=(8, 4))
    plt.scatter(df[xvar], df[yvar], alpha=0.7)
    plt.title(f"{xvar} \nvs.\n {yvar}")
    return


@app.cell
def __(df, mo, xvar, yvar):
    xdf = df[['geo_id', xvar, yvar]]
    mo.plain(xdf)
    return (xdf,)


@app.cell
def __():
    from pathlib import Path
    import pandas as pd
    import matplotlib.pyplot as plt

    READ_PATH = 'data/state_census.csv'
    df = pd.read_csv(READ_PATH)

    # _div = df.columns.difference(['total_pop', 'geo_id']) 
    # df[_div] = df[_div].div(df['total_pop'], axis=0)
    return Path, READ_PATH, df, pd, plt


@app.cell
def __(df, mo):
    xvar_picker = mo.ui.dropdown(
        options=list(df.columns),
        value='median_income'
    )

    yvar_picker =  mo.ui.dropdown(
        options=list(df.columns),
        value='poverty'
    )
    return xvar_picker, yvar_picker


@app.cell
def __(xvar_picker, yvar_picker):
    xvar = xvar_picker.value
    yvar = yvar_picker.value
    return xvar, yvar


if __name__ == "__main__":
    app.run()
