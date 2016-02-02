import requests

def _url(path):
        return 'https://ws.webtrends.com/v3/Reporting/' + path

class WebtrendsAPIWrapper(object):

    def __init__(self, username=None, password=None, response_format="json"):
        self.username = username
        self.password = password
        if response_format is "json":
            self.format_string = "?format=json"

    def get_report_data(self):
        pass

    def get_report_meta(self):
        pass

    # List of available spaces
    def list_spaces(self):
        return requests.get(_url("spaces/" + self.format_string), auth=(self.username, self.password))

    # List available profiles. Option to filer by space ID.
    # (Space ID can be obtained from the ID param of any of the spaces returned by list_spaces)
    def list_profiles(self, space_id=None):
        if space_id is not None:
            return requests.get(_url("spaces/" + str(space_id) + "/profiles/" + self.format_string), auth=(self.username, self.password))
        else:
            return requests.get(_url("profiles/" + self.format_string), auth=(self.username, self.password))

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