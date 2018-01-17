import unittest

from SCMSHTTPRequest import *

class TestCaseAllTests(unittest.TestCase):

        def test_ObeIdBlacklistResponse(self):
            scms_response = send_obe_blacklist_request({"process":"sendObeIdBlRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>",request_response)

        def test_sendLCIRequest(self):
            scms_response = send_lci_request({"process":"sendLCIRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

        def test_sendLIRequest(self):
            scms_response = send_linkage_information_request({"process":"sendLIRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

        def test_sendLSRequest(self):
            scms_response = send_linkage_seed_request({"process":"sendLSRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

        def test_blacklistRequest(self):
            scms_response = send_blacklist_request({"process":"blacklistRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

        def test_sendHPCRRequest(self):
            scms_response = send_hpcr_request({"process":"sendHPCRRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

        def test_sendPLVRequest(self):
            scms_response = send_prelinkage_value_request({"process":"sendPLVRequest"})
            request_response = str(scms_response)
            self.assertEquals("<Response [200]>", request_response)

if __name__ == '__main__':
    unittest.main()