import streamlit as st
import process_backend
import os
import altair as alt
st.set_page_config(layout="wide")

if __name__ == "__main__":

    # Setup Navigation Side Bar
    file_selector = st.sidebar.file_uploader("Select Data File")
    if file_selector is not None:
        data_class = process_backend.DataSet(file_selector)

        data = data_class.main_data
        # Set up master handler for all components
        component_types = {'Pressure': 'PT',
                           'Flow Rate': 'FM',
                           'Valve': 'Valve'}
        selection_containers = []
        all_checkboxes = []
        all_checkbox_entries = []
        for comp in component_types.keys():
            selection_containers.append(st.beta_expander('%s Selector' % comp, expanded=True))
            with selection_containers[-1]:
                # Sensor check-boxes
                checkbox_entries = [data_class.columns[x] for x in data_class.columns.keys() if component_types[comp] in data_class.columns[x]]
                checkboxes = []
                all_checkbox_entries += checkbox_entries
                columns = st.beta_columns(4)
                a = 0
                for cb in checkbox_entries:
                    checkboxes.append(columns[a].checkbox(cb))
                    a += 1
                    if a > len(columns)-1:
                        a = 0
                all_checkboxes += checkboxes

        # Create plot dropdown window
        plot_container = st.beta_expander('Plots', expanded=True)
        with plot_container:
            x_range = st.slider("Plot Range", data_class.min_bound, data_class.max_bound, (data_class.min_bound, data_class.max_bound), 0.5)
            for selected, label in zip(all_checkboxes, all_checkbox_entries):
                if selected is True:
                    data_to_plot = data_class.get_data_by_label(label)
                    data_to_plot = data_to_plot[data_to_plot['Time (s)'] >= x_range[0]]
                    data_to_plot = data_to_plot[data_to_plot['Time (s)'] <= x_range[1]]

                    c = alt.Chart(data_to_plot).mark_line(color="#FFAA00").encode(
                        x='Time (s)',
                        y=label)
                    st.altair_chart(c, use_container_width=True)



