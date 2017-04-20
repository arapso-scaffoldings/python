import logging
import time
from urlparse import urljoin

import requests

API_ENDPOINT = 'https://api.appnexus.com'

AUTH_PATH = urljoin(API_ENDPOINT, 'auth')

REPORT_STATUS_PATH = urljoin(API_ENDPOINT, 'report')

REPORT_META_PATH = urljoin(API_ENDPOINT, 'report')


def report_status(api_username, api_password, report_id):

    try:
        logging.info('Sending request to AppNexus API')
        with requests.Session() as session:
            auth_response = session.post(AUTH_PATH, json=_auth_payload(api_username, api_password))
            auth_response.raise_for_status()
            report_ready = _wait_until(_check_status(session, report_id), 30, 10)
            if report_ready:
                logging.info('Report status...')
                print report_ready
            else:
                logging.error("Report generation timeout, please check the report status, id: '%s'", report_id)
                raise IOError('Report generation timeout')
    except requests.exceptions.RequestException as e:
        logging.error("AppNexus API connection error")
        raise IOError('AppNexus API connection error')


def reports_meta(api_username, api_password):

    try:
        logging.info('Sending request to AppNexus API')
        with requests.Session() as session:
            auth_response = session.post(AUTH_PATH, json=_auth_payload(api_username, api_password))
            auth_response.raise_for_status()
            _check_meta(session=session)
    except requests.exceptions.RequestException as e:
        logging.error("AppNexus API connection error")
        raise IOError('AppNexus API connection error')




def _auth_payload(username, password):
    return {
        'auth': {
            'username': username,
            'password': password
        }
    }


def _wait_until(predicate, period, iterations):
    """
    Check whether predicate is met or number of iterations is exhausted
    :param predicate:  function with predicate
    :param period:     number of seconds to sleep after predicate call
    :param iterations: number of iterations
    :return: True if predicate is met, otherwise False
    """
    i = 0
    result = predicate()
    while i < iterations and result is False:
        time.sleep(period)
        result = predicate()
        i += 1
    return result


def _check_status(session, report_id):
    def f():
        try:
            logging.info("Try to get report status for id: '%s'", report_id)
            status_response = session.get(REPORT_STATUS_PATH, params={'id': report_id})
            status_response.raise_for_status()
            print status_response.text
            return status_response.json()['response']['execution_status'] == 'ready'
        except requests.exceptions.RequestException as e:
            logging.warn("Appnexus api response with error. Retrying...")
            return False

    return f


def _check_meta(session):
    try:
        logging.info("Try to get all reports meta")

        status_response = session.get("https://api.appnexus.com/report?meta=network_device_analytics")
        status_response.raise_for_status()
        print status_response.text
        return True
    except requests.exceptions.RequestException as e:
        logging.warn("Appnexus api response with error. Retrying...")
        return False


if __name__ == "__main__":
    reports_meta("roqadapi","ApiRoq!!!12222")