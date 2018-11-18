import math
import numpy as np
import pandas as pd
import plotly.offline as po
import plotly.graph_objs as go

def fetch_camper_history_statistics(campers_with_cancer_file, siblings_file):
    campers_with_cancer_data = pd.read_csv(campers_with_cancer_file)
    campers_with_cancer_data = campers_with_cancer_data.fillna(0)
    campers_with_cancer_data = campers_with_cancer_data.set_index('Year')
    siblings_data = pd.read_csv(siblings_file)
    siblings_data = siblings_data.fillna(0)
    siblings_data = siblings_data.set_index('Year')
    return campers_with_cancer_data, siblings_data

def create_camper_history_charts(campers_with_cancer_file, siblings_file, output_filename):
    campers_with_cancer_data, siblings_data = fetch_camper_history_statistics(campers_with_cancer_file, siblings_file)
    categories = campers_with_cancer_data.columns
    all_campers_data = campers_with_cancer_data.add(siblings_data, fill_value=0)
    build_aggregate_history_charts(all_campers_data, categories, output_filename)
    build_summary_charts_by_category(campers_with_cancer_data, siblings_data, categories, output_filename)

def build_summary_charts_by_category(campers_with_cancer_data, siblings_data, categories, output_filename):
    line_charts_list = prepare_category_bar_charts(campers_with_cancer_data, siblings_data, categories)
    line_charts_layout = prepare_line_charts_layout(categories)
    fig = dict(data = line_charts_list,
               layout = line_charts_layout)
    filename_components = output_filename.split(".")
    po.plot(fig, filename_components[0] + "_category_summaries." + filename_components[1])

def prepare_category_bar_charts(campers_with_cancer_data, siblings_data, categories):
    x_axis_vals = campers_with_cancer_data.index
    traces = []
    for idx in range(len(categories)):
        category = categories[idx]
        traces.append(add_line_chart(x_axis_vals, campers_with_cancer_data[category], "Campers", category, idx))
        traces.append(add_line_chart(x_axis_vals, siblings_data[category], "Siblings", category, idx))
    return traces

def add_line_chart(x_vals, y_vals, category_suffix, category_name, idx):
    return go.Scatter(x = x_vals,
                      y = y_vals,
                      mode = 'lines+markers',
                      name = category_name + " " + category_suffix,
                      xaxis = "x" + str(idx + 1),
                      yaxis = "y" + str(idx + 1))

def build_aggregate_history_charts(all_campers_data, categories, output_filename):
    aggregate_time_series_data = generate_aggregate_time_series(all_campers_data, categories)
    pie_chart_data = generate_pie_chart(all_campers_data, categories)
    aggregate_layout = build_aggregate_history_layout()
    fig = dict(data = [*aggregate_time_series_data, pie_chart_data],
               layout = aggregate_layout)
    filename_components = output_filename.split(".")
    po.plot(fig, filename = filename_components[0] + "_aggregate." + filename_components[1])

def generate_aggregate_time_series(all_campers_data, categories):
    x_axis_vals = all_campers_data.index
    lines = [None for _ in range(len(categories))]
    for idx in range(len(categories)):
        category = categories[idx]
        line_data = go.Scatter(x = x_axis_vals,
                               y = all_campers_data[category],
                               mode = 'lines+markers',
                               name = category,
                               xaxis = 'x1',
                               yaxis = 'y1')
        lines[idx] = line_data
    return lines

def generate_pie_chart(all_campers_data, categories):
    summary_data = all_campers_data.sum()
    return go.Pie(labels = summary_data.index,
                  values = summary_data.values,
                  hoverinfo = 'label+percent',
                  textinfo = 'value',
                  textfont = dict(size=20),
                  domain = dict(x = [0.0, 1.0], y = [0.0, 0.5]))

def build_aggregate_history_layout():
    return dict(
            width = 1200,
            height = 800,
            title = "Camp Enrollment Statistics",
            xaxis1 = dict(domain=[0.0, 1.0], anchor = 'y1', tickangle = -30, dtick = 2),
            yaxis1 = dict(domain=[0.55, 1.0], title="Count", anchor = 'x1'))

def prepare_line_charts_layout(categories):
    category_count = len(categories)
    row_size = determine_row_size(category_count)
    layout_dict = dict(width = 1200, height= 800, title = "Camp Enrollment by Location")
    for idx in range(category_count):
        layout_dict = add_axes_for_index(layout_dict, row_size, idx)
    return layout_dict

def determine_row_size(category_count):
    number_of_rows = math.ceil(category_count / 2)
    number_of_gaps = number_of_rows - 1
    return (1 - (0.05 * number_of_gaps)) / number_of_rows

def add_axes_for_index(layout_dict, row_size, idx):
    column_range = [0.0, 0.45] if (idx % 2 == 0) else [0.55, 1.0]
    row_index = math.ceil((idx + 1) / 2)
    row_upper_bound = 1 - ((row_size + 0.05) * (row_index - 1))
    row_lower_bound = 1 - ((row_size + 0.05) * (row_index - 1)) - row_size
    idx_str = str(idx + 1)
    layout_dict['xaxis' + idx_str] = dict(domain=column_range, anchor= "y" + idx_str, tickangle = -30, dtick = 4)
    layout_dict['yaxis' + idx_str] = dict(domain=[max(0,row_lower_bound), row_upper_bound], title = "Count", anchor = "x" + idx_str)
    return layout_dict
