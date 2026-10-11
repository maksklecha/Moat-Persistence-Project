"""Display three years of Apple financial statements from an uploaded workbook."""

import pandas as pd
from google.colab import files

# 1. Upload your completed Excel workbook.
uploaded = files.upload()
filename = next(iter(uploaded))

# 2. Read the financial table.
table = pd.read_excel(
    filename,
    sheet_name="Apple financials",
    header=5,        # Column headings are in Excel row 6.
    usecols="B:E",   # Metric, 2023, 2024 and 2025.
    nrows=9,
)

# 3. Use metric names as row labels.
table = table.set_index("Metric")
table.columns = [str(year) for year in table.columns]

# 4. Display the table.
print("Apple — financial statements")
print("All figures in USD millions")

display(table.style.format("{:,.0f}", na_rep="Missing"))
