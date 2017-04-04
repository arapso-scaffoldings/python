import os
import boto
from boto.s3.key import Key
import logging


class S3Client:

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, host='s3.eu-central-1.amazonaws.com'):
        """
        Initialization of S3 client with credentials.
        When no credentials given system user credentials will be used from ${HOME}/.aws/credentials file
        Optionally we can change s3 region by providing s3 host url from that region
        """
        os.environ['S3_USE_SIGV4'] = 'True'  # We must force boto to use specific signature method

        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.host = host

    def copy_files_to_local(self, bucket_name, prefix, output_dir):
        """
        Enables to copy files from specific bucket from s3 to local directory.
        Prefix should be suppliet otherwise all content of s3 bucket will be tried to download.

        S3 has flat structure so there is no directories abstraction.

        Example
        We need to download all events for requested report date from s3 bucket.
        Files with described by urls below are in s3 bucket
            s3://roqad-logs/dsp/events/2017-03-10/events_2017-03-10-1489104106289.json
            s3://roqad-logs/dsp/events/2017-03-10/events_2017-03-10-1489104106539.json

        To download all those file we should invoke method like:
            client.copy_files_to_local("roqad_logs", "dsp/events/2017-03-02/", "./result")

        After that all files will be available in local directory result with name without prefix part of url
            ./result/events_2017-03-10-1489104106289.json
            ./result/events_2017-03-10-1489104106539.json

        :param bucket_name: s3 bucket name
        :param prefix: 'directory' on s3 to download files from
        :param output_dir: local directory where downloaded files will be saved
        """
        logging.info("Downloading files from s3://%s/%s to directory %s'", bucket_name, prefix, output_dir)

        self.__ensure_output_dir_exists(output_dir)
        conn = boto.connect_s3(self.aws_access_key_id, self.aws_secret_access_key, host=self.host)
        bucket = conn.get_bucket(bucket_name)
        events_files = bucket.list(prefix)
        for s3_object in events_files:
            logging.info("\tDownloading file: '%s'", s3_object.key)
            file_key = Key(bucket=bucket, name=s3_object.key)
            output_file_path = os.path.join(output_dir, os.path.basename(s3_object.key))
            with open(output_file_path, 'w') as result_file:
                file_key.get_contents_to_file(result_file)
        logging.info("All files copied to local directory")

    @staticmethod
    def __ensure_output_dir_exists(output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if not os.path.isdir(output_dir):
            raise Exception("Requested output path is not directory.")
