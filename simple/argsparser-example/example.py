import argparse


parser = argparse.ArgumentParser(description='Script, which starts Spot Instances into AWS EC2',
                                     usage='%(prog)s [options]')
parser.add_argument('--servers-group', type=str, required=True,
                        help='The identifier of the group of server in AWS EC2 of single Spark Clusters. ')
parser.add_argument('--master-dns', type=str, required=True,
                        help='The public DNS under which Spark Master can be reachable')
parser.add_argument('--master-allocation-id', type=str, required=True,
                        help='The allocation id for Elastic IP Address, which should be assigned to master.')

parser.add_argument('--slave-instances-count', type=int, required=True,
                        help='Number of instances that will be created.')

parser.add_argument('--placement-group', type=str, required=False,
                        help='Name of the Placement Group (must be given if advanced networking is to be used)')

parser.add_argument('--accepted-slave-instance-types', type=str, required=True,
                        nargs="*", choices=['a', 'b', 'c'],
                        help='EC2 slave machine instance types (API Name, like r2.8xlarge, for multiple types '
                             'separate names with whitespaces)')
gs = parser.parse_args("--master-dns s "
                       "--servers-group ad --master-allocation-id ad "
                       "--slave-instances-count 2 "
                       "--accepted-slave-instance-types a ad".split())

print gs.accepted_slave_instance_types