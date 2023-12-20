'''Return a list of entra groups for the JAMF enrolled user'''

from __future__ import absolute_import, print_function

import os
import sys

sys.path.append('/usr/local/munki')
try:
    from munkilib import FoundationPlist
except ImportError:
    print('ERROR: Cannot import FoundationPlist')
    sys.exit(1)


def fact():
    '''Return the list of entra groups for the JAMF enrolled user'''
    return {'entra_ad_groups': get_entra_groups()}

def get_entra_groups():
    """Read groups from /usr/local/matw/config/groups.plist."""
    # target = 'Display Menu'
    group_list_dir = '/usr/local/matw/config'
    group_list_name = 'groups'
    group_list_path = f'{group_list_dir}/{group_list_name}.plist'

    if os.path.exists(group_list_path):
        try:
            groups_plist =  FoundationPlist.readPlist(group_list_path)
        except FoundationPlist.NSPropertyListSerializationException:
            print(f'ERROR: Cannot read {group_list_path}')
            sys.exit(1)

        entra_groups = list(groups_plist['Entra_AD_Groups'])
        return(entra_groups)

    return([])


if __name__ == '__main__':
    print(fact())













#!/usr/local/munki/munki-python




