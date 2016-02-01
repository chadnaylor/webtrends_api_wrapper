import requests

class WebtrendsAPIWrapper(object):
    url = "https://ws.webtrends.com/v3/Reporting/"

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def get_report_data(self):
        pass

    def get_report_meta(self):
        pass

    def list_spaces(self):
        return requests.get(self.url + "spaces/?format=json")

    def list_profiles(self):
        pass

    def list_reports(self):
        pass

    ### START Methods TBD (Probably won't need these for a while)
    def get_key_metrics_for_a_profile(self):
        pass

    def get_key_metrics_for_all_profiles_in_a_space(self):
        pass

    def get_key_metrics_for_default_profiles_of_all_spaces(self):
        pass
    ### END Methods TBD