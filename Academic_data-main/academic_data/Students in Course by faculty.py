import plotly.express as px
import numpy as np
import pandas as pd
from pathlib import Path
import os
total_degress = ["Undergraduate", "Masters", "PhD", "M.Tech"]
color_code = {"Undergraduate": "blue",
              "Masters": "green",
              "PhD": "red",
              "M.Tech": "brown"}


def drop_courses(df):
    new_df = df.drop(np.where(df["Students"] == 0)[0])
    return new_df


def classify(roll):
    if roll[2] == '0':
        return "Undergraduate"
    elif roll[2] == '1':
        return "Masters"
    elif roll[2] == '2':
        return "PhD"
    elif roll[2] == '3':
        return "M.Tech"


def create_df(branch_name: str):
    base_path = r"C:\Users\Ninad\OneDrive\Desktop\Academic_dataProject\Academic_data-main\academic_data\Year_2021\2022-2023 Autumn\{branch_name}".format(
        branch_name=branch_name)
    values = pd.DataFrame()
    for file in os.listdir(base_path):
        if (not file.endswith(".csv")):
            continue
        path = os.path.join(base_path, file)
        df = pd.read_csv(path, usecols=["Roll No."])

        df['Roll No.'] = df['Roll No.'].astype(str)
        df['Degree'] = df['Roll No.'].apply(classify)
        df = df.groupby(["Degree"]).count()
        df.rename(columns={"Roll No.": "Students"}, inplace=True)

        df["Course"] = file[0:6]
        df["Deg"] = df.index
        if df.empty:
            df["Students"] = [0]
            df["Course"] = file[0:6]
            df["Deg"] = ["Undergraduate"]

        if (values.empty):
            values = df
        else:
            values = values.merge(df, how="outer")
    # values.sort_values(by="Deg",ascending=False,inplace=False)
    # values.sort_values(by="Course",ascending=True,inplace=True)
    values.fillna(0, inplace=True)
    return values


branch_name = "Mathematics"
# branches = ['Biology', 'Chemistry', 'Civil', 'Computer Science', 'Electrical', 'HSS',
#             'Mathematics', 'Mechanical', 'Physics']
path = r"C:\Users\Ninad\OneDrive\Desktop\Academic_dataProject\Academic_data-main\academic_data\Year_2021\2022-2023 Autumn"
if not os.path.exists(path):
    os.mkdir(path)
# for branch_name in branches:
values = create_df(branch_name)
values = drop_courses(values)
print(values.drop(np.where(values["Students"] == 0)[0]))
import plotly.graph_objects as go
fig = go.Figure()

values.sort_values(by="Deg", ascending=False, inplace=False)
fig = px.bar(values, x="Course", y="Students", title="Division of Students",
                color="Deg", color_discrete_map=color_code,barmode="group",text="Students")
fig.update_traces(textfont_size=20, textangle=0,
                  textposition="outside", showlegend=False)

fig.update_xaxes(tickangle=-90)
fig.update_layout(font_size=20)

# fig.write_image(os.path.join(path,branch_name+".png"))
fig.show()


# For adding misssing degrees
# missing_degrees=set(total_degress)-set(values["Deg"].unique())
# for i in missing_degrees:
#     df=pd.DataFrame(columns=["Students","Course","Deg"])
#     df["Students"]=[0]
#     df["Course"]=values["Course"].loc[0]
#     df["Deg"]=i
#     values=pd.concat([values,df],ignore_index=True)
