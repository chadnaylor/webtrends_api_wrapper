import requests

def _url(path):
        return 'https://ws.webtrends.com/v3/Reporting/' + path
class WebtrendsAPIWrapper(object):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password



    def get_report_data(self):
        pass

    def get_report_meta(self):
        pass

    def list_spaces(self):
        return requests.get(_url("spaces/?format=json"), auth=(self.username, self.password))

    def list_profiles(self, space=None):
        return requests.get(_url("profiles/?format=json"), auth=(self.username, self.password))

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