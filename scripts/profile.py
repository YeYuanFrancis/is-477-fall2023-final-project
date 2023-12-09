from ydata_profiling import ProfileReport
import pandas as pd
df = pd.read_csv('data/wine/wine.data')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")