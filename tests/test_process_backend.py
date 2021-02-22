from unittest import TestCase


class TestDataSet(TestCase):
    def test_data_set(self):
        from process_backend import DataSet
        path = 'C6_GSS_PIPING_START-2021-02-18T21_45_00.000Z_END-2021-02-18T22_41_00.000Z.csv'
        data = DataSet(path)

        print(data)

    def test_main_data(self):
        from process_backend import DataSet
        path = 'C6_GSS_PIPING_START-2021-02-18T21_45_00.000Z_END-2021-02-18T22_41_00.000Z.csv'
        data_class = DataSet(path)
        main = data_class.main_data
