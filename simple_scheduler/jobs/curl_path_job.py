"""A job to send a HTTP (GET or DELETE) periodically."""

import logging
import requests
import os

from ndscheduler.corescheduler import job

logger = logging.getLogger(__name__)


class CurlPathJob(job.JobBase):

    @classmethod
    def meta_info(cls):
        url_name = os.getenv("CURL_PATH_URL", "http://localhost/api/v1/")
        return {
            "job_class_string": "%s.%s" % (cls.__module__, cls.__name__),
            "notes": "This sends a HTTP GET request to %s" % (url_name),
            "arguments": [
                # path
                {"type": "string", "description": "what path do we add to this request", },
                
            ],
            "example_arguments": (
                '["jobs"]' 
            ),
        }

    def run(self, path, *args, **kwargs):
        url_name = os.getenv("CURL_PATH_URL", "http://localhost/api/v1/")
        url = "%s%s" % (url_name, path)
        print("Start GET on url: %s" % (url))

        session = requests.Session()
        result = session.request(request_type, url, headers=None, data=None)
        print("Calling GET on url: %s" % (url))
        return result.text


if __name__ == "__main__":
    job = CurlPathJob.create_test_instance()
    job.run("http://localhost:888/api/v1/jobs")
