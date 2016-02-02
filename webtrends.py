import requests

def _url(path):
        return 'https://ws.webtrends.com/v3/Reporting/' + path

class WebtrendsAPIWrapper(object):

    def __init__(self, username=None, password=None, response_format="json"):
        self.username = username
        self.password = password
        if response_format is "json":
            self.format_string = "?format=json"

    def get_report_data(self, profile, report, totals="all", start_period="current_month-1", end_period="current_month",
                        period_type="agg"):
        """
        Get data from a report. Must supply profile and report
        :param profile:
        :param report:
        :param totals:
        :param start_period:
        :param end_period:
        :param period_type:
        :return: response object
        """
        filters_string = "&totals=" + totals + "&start_period=" + start_period + "&end_period=" + end_period + \
                         "&period_type=" + period_type
        return requests.get(_url("profiles/" + str(profile) + "/reports/" + str(report) + "/" + self.format_string +
                                 filters_string), auth=(self.username, self.password))

    def get_report_meta(self):
        pass

    def list_spaces(self):
        """
        List of available spaces
        :return: response object
        """
        return requests.get(_url("spaces/" + self.format_string), auth=(self.username, self.password))

    def list_profiles(self, space_id=None):
        """
        List available profiles. Option to filer by space ID.
        :param space_id: Int Space ID can be obtained from the ID param of any of the spaces returned by list_spaces
        :return: response object
        """
        if space_id is not None:
            return requests.get(_url("spaces/" + str(space_id) + "/profiles/" + self.format_string), auth=(self.username, self.password))
        else:
            return requests.get(_url("profiles/" + self.format_string), auth=(self.username, self.password))

    def list_reports(self, profile_id):
        """
        List available reports for a given profile. Must provide profile ID.
        :param profile_id: Int Profile ID can be obtained from the ID param of the profiles returned by list_profiles
        :return: response object
        """
        return requests.get(_url("profiles/" + str(profile_id) + "/reports/" + self.format_string), auth=(self.username, self.password))

    ### START Methods TBD (Probably won't need these for a while)
    def get_key_metrics_for_a_profile(self):
        pass

    def get_key_metrics_for_all_profiles_in_a_space(self):
        pass

    def get_key_metrics_for_default_profiles_of_all_spaces(self):
        pass
    ### END Methods TBD