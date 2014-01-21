import unittest
from config.configuration import Configuration
from config.config_gateway.in_memory import InMemoryConfigFileGateway
from config.config_gateway.base_config_file_gateway import ConfigValueNotSetException,\
    CorruptConfigFileException

class ConfigurationTest(unittest.TestCase):
    
    def setUp(self):
        self.gateway =  InMemoryConfigFileGateway()
        Configuration.gateway = self.gateway
    
    def test_if_missing_attribute_then_raise_exception_with_info_about_missing_field(self):
        try:
            Configuration().get_email_address()
            self.fail("Should have raised exception")
        except ConfigValueNotSetException, e:
            self.assertEquals('email_address', e.field_name)
            
    def test_if_file_is_not_valid_json_dict_then_raise_exception(self):
        self.gateway.save_data("not valid JSON")
        self.assertRaises(CorruptConfigFileException, Configuration.get_email_address)
        
        self.gateway.save_json(['still bad data because we want a dictionary and not a list'])
        self.assertRaises(CorruptConfigFileException, Configuration.get_email_address)

    def test_if_config_value_is_set_then_return_from_file(self):
        self.gateway.save_json({'email_address': "Happy Days"})
        self.assertEquals("Happy Days", Configuration.get_email_address())

    def test_can_set_config_value_on_empty_file(self):
        Configuration.set_email_address('some_attribute_value')
        self.assertEquals('some_attribute_value', Configuration.get_email_address())
    
    def test_can_save_and_get_password(self):
        Configuration.set_password('secret')
        self.assertEquals('secret', Configuration.get_password())

    def test_password_is_stored_in_a_way_that_looks_like_it_encrypted(self):
        Configuration.set_password('secret')
        self.assertNotEquals('secret', self.gateway.get_json()['password'])
    
    def test_updating_config_does_not_override_other_entries(self):
        Configuration.set_password('existed')
        Configuration.set_email_address('some_attribute_value')
        self.assertEquals('some_attribute_value', Configuration.get_email_address())
        self.assertEquals('existed', Configuration.get_password())
        