import unittest
from webtrends import WebtrendsAPIWrapper
import auth
import json
import requests

class TestWebtrendsAPIWrapper(unittest.TestCase):

    def test_get_report_data(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        response = wrapper.get_report_data(profile_id, report_id)
        self.assertEqual(200, response.status_code)

    def test_get_report_data_with_current_day(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # Test past day
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_day-1", end_period="current_day")
        self.assertEqual(200, response.status_code)

        # Test past ten days
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_day-10", end_period="current_day")
        self.assertEqual(200, response.status_code)

    def test_get_report_data_with_current_hour(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # Test past hour
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_hour-1", end_period="current_hour")
        self.assertEqual(200, response.status_code)

        # Test past ten hours
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_hour-10", end_period="current_hour")
        self.assertEqual(200, response.status_code)

    def test_get_report_data_with_current_month(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # Test past month
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_month-1", end_period="current_month")
        self.assertEqual(200, response.status_code)

        # Test past ten months
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_month-10", end_period="current_month")
        self.assertEqual(200, response.status_code)
    
    def test_get_report_data_with_current_year(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # Test past year
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_year-1", end_period="current_year")
        self.assertEqual(200, response.status_code)

        # Test past ten years
        response = wrapper.get_report_data(profile_id, report_id, start_period="current_year-10", end_period="current_year")
        self.assertEqual(200, response.status_code)

    def test_get_report_data_with_absolute_time(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # January 2016
        response = wrapper.get_report_data(profile_id, report_id, start_period="2016m01d01h00", end_period="2016m02d01h00")
        self.assertEqual(200, response.status_code)
    
    def test_get_report_data_with_conflicting_time_params(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        # Make request with different types of relative time params for start_period and end_period
        # Should get a 400 BAD REQUEST response
        self.assertRaises(requests.exceptions.HTTPError, wrapper.get_report_data, profile_id, report_id, start_period="current_day-1", end_period="current_month")
    
    def test_get_report_meta(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        # Get the id of a report
        reports = json.loads(wrapper.list_reports(profile_id).text)
        report_id = reports[0]["ID"]

        response = wrapper.get_report_meta(profile_id, report_id)
        self.assertEqual(200, response.status_code)
    
    def test_list_spaces(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)
        response = wrapper.list_spaces()
        self.assertEqual(200, response.status_code)

    def test_list_profiles(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)
        response = wrapper.list_profiles()
        self.assertEqual(200, response.status_code)

    def test_list_profiles_with_space(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a space
        spaces = json.loads(wrapper.list_spaces().text)
        space_id = spaces[0]["ID"]

        # Ask for profiles only in the requested space
        response = wrapper.list_profiles(space_id)
        self.assertEqual(200, response.status_code)

        # Verify That profiles are only in requested space
        response_profiles = json.loads(response.text)
        for profile in response_profiles:
            self.assertEqual(space_id, profile["SpaceID"])
    
    def test_list_reports(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)

        # Get the id of a profile
        profiles = json.loads(wrapper.list_profiles().text)
        profile_id = profiles[0]["ID"]

        response = wrapper.list_reports(profile_id)
        self.assertEqual(200, response.status_code)

    ### START Methods TBD (Probably won't need these for a while)
    @unittest.skip("Method TBD")
    def test_get_key_metrics_for_a_profile(self):
        pass

    @unittest.skip("Method TBD")
    def test_get_key_metrics_for_all_profiles_in_a_space(self):
        pass

    @unittest.skip("Method TBD")
    def test_get_key_metrics_for_default_profiles_of_all_spaces(self):
        pass
    ### END Methods TBD

if __name__ == '__main__':
    unittest.main()
