import unittest
from webtrends import WebtrendsAPIWrapper
import auth
import json

class TestWebtrendsAPIWrapper(unittest.TestCase):
    def test_get_report_data(self):
        pass
    
    def test_get_report_meta(self):
        pass
    
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
            self.assertEqual(space_id, profile["ID"])
    
    def test_list_reports(self):
        wrapper = WebtrendsAPIWrapper(username=auth.username, password=auth.password)
        response = wrapper.list_reports()
        self.assertEqual(200, response.status_code)

    ### START Methods TBD (Probably won't need these for a while)
    def test_get_key_metrics_for_a_profile(self):
        pass
    
    def test_get_key_metrics_for_all_profiles_in_a_space(self):
        pass
    
    def test_get_key_metrics_for_default_profiles_of_all_spaces(self):
        pass
    ### END Methods TBD

if __name__ == '__main__':
    unittest.main()
