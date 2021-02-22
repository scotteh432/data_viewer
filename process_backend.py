import pandas as pd
import os

__root__ = os.path.dirname(os.path.realpath(__file__))


class DataSet:
    def __init__(self, path_to_data_set):
        self._database = pd.read_csv(path_to_data_set)
        self._database['Time (s)'] = (self._database['epoch_ts'] - list(self._database['epoch_ts'])[0])/1000
        self._column_legend = {
            'tran_10v_1_status': 'FT-PT (Fuel Tank Pressure)',
            'tran_10v_2_status': 'PFLF-PT-2',
            'tran_10v_3_status': 'PFLF-PT-1',
            'tran_10v_4_status': '',
            'tran_10v_5_status': 'PR-PT-F',
            'tran_10v_6_status': 'PR-PT-O',
            'tran_10v_7_status': 'PR-PT (Feed Box Pressure)',
            'tran_10v_8_status': 'PR-PT-E',
            'tran_10v_9_status': 'PS-PT (Supply Box Pressure)',
            'tran_30mv_1_status': 'OT-PT (LOX Tank Pressure)',
            'tran_30mv_2_status': 'PFLO-PT-2',
            'tran_30mv_3_status': 'PFLO-PT-1',
            'tran_10v_10_status': 'PFLO-FM (LOX Flow Rate)',
            'tran_10v_11_status': 'PFLF-FM (Fuel Flow Rate)',

            'valve1_status': 'Valve 1',
            'valve2_status': 'Valve 2',
            'valve3_status': 'Valve 3',
            'valve4_status': 'Valve 4',
            'valve5_status': 'Valve 5',
            'valve6_status': 'Valve 6',
            'valve7_status': 'Valve 7',
            'valve8_status': 'Valve 8',
            'valve9_status': 'Valve 9',
            'valve10_status': 'Valve 10',
            'valve11_status': 'Valve 11',
            'valve12_status': 'Valve 12',
            'valve13_status': 'Valve 13',
        }

    def get_data_by_label(self, label):
        foo = self.main_data
        data = pd.DataFrame({})
        data['Time (s)'] = foo['Time (s)']
        data[label] = foo[label]
        return data

    def get_data_by_labels(self, labels):
        foo = self.main_data
        data = pd.DataFrame({})
        data['Time (s)'] = foo['Time (s)']
        for label in labels:
            data[label] = foo[label]
        return data

    @property
    def raw_data(self):
        return self._database

    @property
    def main_data(self):
        data = pd.DataFrame({})
        data['Time (s)'] = self._database['Time (s)']
        for key in self.columns.keys():
            data[self.columns[key]] = self._database[key]
        return data

    @property
    def columns(self):
        return self._column_legend

    @property
    def min_bound(self):
        time = self._database['Time (s)']
        return min(time)

    @property
    def max_bound(self):
        time = self._database['Time (s)']
        return max(time)

